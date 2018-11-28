//
//  main.cpp
//  StandingOvation
//
//  Created by Tingting Cao on 11/04/2015.
//  Copyright (c) 2015 Tingting Cao. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

int main(int argc, const char * argv[]) {
    
    int numberOfCase;
    cin>>numberOfCase;
    
    for(int c = 1; c<=numberOfCase; c++)
    {
        //get input
        
        int maxShy;
        string shyDistribute;
        
        cin>>maxShy;
        cin>>shyDistribute;
//        cout<<shyDistribute<<endl;
        
        vector<int> numberOfPeopleHasShyLevel(maxShy+1,0);
        
        for(int i = 0; i<maxShy+1; i++)
        {
            char cur = shyDistribute[i];
            int curInt = cur - 48;
            numberOfPeopleHasShyLevel[i] = curInt;
        }
        
//        for(int i =0;i<numberOfPeopleHasShyLevel.size();i++)
//        {
//            cout<<numberOfPeopleHasShyLevel[i]<<endl;
//        }
        
        int numberOfpeopleNeeded = 0;
        int numberOfPeopleAlredayStandUp = 0;
        
        for(int i =0; i<numberOfPeopleHasShyLevel.size(); i++)
        {
            if(numberOfPeopleAlredayStandUp >= i)
            {
                //means cur leavel people will stand up and clap
                numberOfPeopleAlredayStandUp += numberOfPeopleHasShyLevel[i];
            }
            else
            {
                //means we need people to make the cur level stand up
                int numOfPeopleToAdd = i - numberOfPeopleAlredayStandUp;
                numberOfpeopleNeeded += numOfPeopleToAdd;
                numberOfPeopleAlredayStandUp += numberOfPeopleHasShyLevel[i];
                numberOfPeopleAlredayStandUp += numOfPeopleToAdd;
            }
        }
        
        //calculate output
        
        
        cout<<"Case #"<<c<<": ";
        //output result
        cout<<numberOfpeopleNeeded;
        cout<<endl;
    }
    
    return 0;
}
