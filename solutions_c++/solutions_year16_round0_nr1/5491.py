//
//  main.cpp
//  GoogleJam
//
//  Created by Isira Samarasekera on 3/13/16.
//  Copyright (c) 2016 Isira Samarasekera. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <numeric>

using namespace std;



bool allSet(map<char,bool> countingMap)
{
    if(countingMap.empty())
        return false;
    
    for (auto it = countingMap.begin(); it != countingMap.end(); it++)
    {
        if(!it->second)
        {
            return false;
        }
    }
    return true;
}

string CountingSheep(int N)
{
    if (N== 0)
        return "INSOMNIA";
    map<char,bool> countingMap;
    for(int i = 0 ; i < 10 ; i++)
    {
        countingMap[to_string(i)[0]] = false;
    }
    
    int M ;
    for(M = N; !allSet(countingMap) ; M+=N)
    {

        string NS = to_string(M);
        
        for(auto c : NS)
        {
            countingMap[c] = true;
        }
    }


    return to_string(M-N);
}


int main(int argc, const char * argv[]) {
    // insert code here...
    ifstream in("/Users/isira/Documents/Semester_4/Social_Media_Mining/Homework/A-large.in");
    ofstream out("/Users/isira/Documents/B-small-practice.out");
    string line;
    getline(in, line);
    
    int nTests =0;
    nTests = stoi(line);
    for(int i= 0; i < nTests; i++)
    {
        getline(in, line);
        int N =stoi(line);   // number of milkshakes
        
        //cout<<N<<endl;
        /*
        getline(in, line);

        int M = stoi(line); // Number of clients
        
        vector<vector<pair<int,int>>> clientChoices;
        
        for(int j =0; j < M; j++)
        {
            string item;
            getline(in, line);
            stringstream ss(line);
            getline(ss, item, ' ');
            
            int T  = stoi(item);
            vector<pair<int,int> > choices;
            for(int k =0; k < T; k++)
            {
                getline(ss, item, ' ');
                int MilkShakeType = stoi(item);
                getline(ss, item, ' ');
                int molted =  stoi(item);
                
                choices.emplace_back(MilkShakeType,molted);
            }
            clientChoices.emplace_back(choices);

        }
        
        vector<int> results = Milkshakes(clientChoices, N);
         
        */
        
        out<<"Case #"<<i+1 <<": "<<CountingSheep(N);
        out<<endl;

    }

    in.close();
    out.close();

    return 0;
}
