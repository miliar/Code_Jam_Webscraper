//
//  main.cpp
//  Magic_Trick
//
//  Created by CuiLei on 4/12/14.
//  Copyright (c) 2014 wolfshow. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[])
{

    // insert code here...
    int T,F,S;
    cin >> T;
    int num;
    for(int ca = 1; ca <= T; ca++)
    {
        cin >> F;
        vector<int> first;
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4;j++)
            {
                cin >> num;
                if(i + 1 == F)
                    first.push_back(num);
            }
        }
        cin >> S;
        vector<int> second;
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4;j++)
            {
                cin >> num;
                if(i + 1 == S)
                    second.push_back(num);
            }
        }
        
        vector<int> res;
        for(int i = 0; i < 4; i++)
        {
            vector<int>::iterator iter = find(second.begin(), second.end(), first[i]);
            if(iter != second.end())
            {
                res.push_back(first[i]);
            }
        }
        if(res.size() == 1)
        {
            cout << "Case #" << ca << ": " << res[0] << endl;
        }
        else if(res.size() > 1)
        {
            cout << "Case #" << ca << ": Bad magician!" << endl;
        }
        else
        {
            cout << "Case #" << ca << ": Volunteer cheated!" << endl;
        }
    }
    
    //std::cout << "Hello, World!\n";
    return 0;
}

