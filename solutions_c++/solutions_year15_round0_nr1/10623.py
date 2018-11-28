//
//  main.cpp
//  standing-ovation
//
//  Created by Xavier Geerinck on 11/04/15.
//  Copyright (c) 2015 Xavier Geerinck. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string.h>

int get_invites_needed(int max_shyness, std::string audience);

int main(int argc, const char * argv[])
{
    std::ifstream in("STDIN");
    std::ofstream out("STDOUT");
    
    if (!in.is_open()) {
        std::cout << "Could not open file." << std::endl;
        exit(EXIT_FAILURE);
    }
    
    int line_count;
    in >> line_count;
    
    //std::cout << "Line Count: " << line_count << std::endl;
    
    for (int i = 0; i < line_count; i++) {
        int max_shyness_level;
        std::string audience_members;
        
        in >> max_shyness_level;
        in >> audience_members;
        
        //std::cout << "Shyness Level: " << max_shyness_level << std::endl;
        //std::cout << "Audience Members: " << audience_members << std::endl;
        
        int invites_needed = get_invites_needed(max_shyness_level, audience_members);
        out << "Case #" << (i + 1) << ": " << invites_needed << std::endl;
    }
    
    
    in.close();
    out.close();
    
    return 0;
}

int get_invites_needed(int max_shyness, std::string audience) {
    int need_to_invite = 0;
    int people_standing = 0;
    
    for (int i = 0; i < (max_shyness + 1); i++) {
        int people_waiting = audience[i] - '0';
        
        //std::cout << "People waiting: " << people_waiting << std::endl;
        
        // If we need people standing, calculate
        if (people_waiting > 0 && people_standing < i) {
            //std::cout << "Need people!" << std::endl;
            need_to_invite += (i - people_standing);
            people_standing += need_to_invite;
        }
        
        // Add people
        people_standing += people_waiting;
        
        //std::cout << "People standing: " << people_standing << std::endl;
        //std::cout << "People need to invite: " << need_to_invite << std::endl;
        
    }
    
    return need_to_invite;
}

