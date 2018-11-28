//
//  main.cpp
//  standing_ovation
//
//  Created by Schlafen on 4/10/15.
//  Copyright (c) 2015 Schlafen. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string.h>
#include <cstdlib>
#include <stdio.h>

//STL library
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    //cout <<"The number of arguments is "<<argc<<endl;
    
    if(argc >= 2) {
        //Start to execute the sequence
        string filename = argv[1];
    
        char cycles_char[4] = {0};
        int cycles = 0;
        //Open the filename
        ifstream file_inst (filename.c_str());
        ofstream file_output;
        file_output.open("bot.out",ios::out);
        file_inst >> cycles_char;
        cycles = atoi(cycles_char);

        //Friends invited variable
        int friends_invited = 0;
    
        //Create array who describes the audience
        vector <int> audience_array;
        for(int i = 0; i<cycles; i++) {
            int max_shyness = 0;
            file_inst >> max_shyness;
            //cout<<"The maximum shyness value is "<<max_shyness<<endl;
            //If there is no array describing the shyness levels, then it will do automatically
            
            char audience_member;//Character used to traverse the file
            for (int c = 0; c<=max_shyness; c++) {
                file_inst>>audience_member;
                audience_array.push_back(atoi(&audience_member));
                //cout <<"The value of next character is "<<audience_array[c]<<endl;
            }
            
            //Traverse the array to find out the minimum number of friends to invite
            int people_clapping = 0;
            //cout<<"The size of audience array is "<<audience_array.size()<<endl;
            for (int c=0; c < audience_array.size(); c++) {
                int new_friend_iteration = 0;
                if(people_clapping >= c) {//People on this level start to clap
                    people_clapping += audience_array[c];
                    //cout<<"People on level "<<c<<" start clapping"<<endl;
                }
                else {
                    //Invite friends, if there is someone to invite in this group
                    //cout<<"The value of audience array is "<<audience_array[c]<<" and c is "<<c<<endl;
                    if(audience_array[c] > 0) {
                        //To make this group clap, I must invite x quantity of friends
                        new_friend_iteration = c - people_clapping;
                        //cout<<"The new value of new friend iteration is "<<new_friend_iteration<<endl;
                        friends_invited += new_friend_iteration;
                        people_clapping += new_friend_iteration+audience_array[c];
                    }
                }
            }
            
            cout<<"Case #"<<i+1<<": "<<friends_invited<<endl;
        
            //Reset the vector
            audience_array.resize(0);
            //Reset friends invited
            friends_invited = 0;
        }
        file_inst.close();
        file_output.close();
    }
    return 0;
}
