//
//  main.cpp
//  A_CountingSheep
//
//  Created by apple on 2016/4/9.
//  Copyright © 2016年 apple. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
void mapping(vector<bool> &map, int N)
{
    int temp = N;
    while (temp>0)
    {
        map[temp%10] = 1;
        temp -= temp%10;
        temp /= 10;
    }
}
bool check(vector<bool> &map)
{
    for (int i = 0; i<10; i++)
    {
        if (map[i]==0) return false;
    }
    return true;
}

int main(int argc, const char * argv[]) {
    // input file
    char line[100];
    int index = 1; // line number
    int num_data; // number of data
    vector<int> input;
    fstream fin;
    fin.open("A-small-attempt1.in",ios::in);
    while(fin.getline(line,sizeof(line),'\n'))
    {
        if (index == 1)
        {
            num_data = atoi(line);
            input.resize(num_data);
        }
        else
        {
            input[index-2] = atoi(line);
        }
        index++;
    }
    for (int i = 0; i <input.size(); i++)
    {
      
    // N
        int N = input[i];
        vector <bool> Map(10,0);
        // infinite
        if (N == 0)
        {
            cout << "Case #" << i+1 << ": INSOMNIA"<< endl;
            continue;
        }
        // finite
        int T = 1;
        while (check(Map) == false)
        {
            mapping(Map, N*T);
            //cout << "(N,T) = (" << N << "," << T << ") //  ";
            //for (int i = 0; i < 10; i++) cout << Map[i];
            //cout << endl;
            T++;
        }
        cout << "Case #" << i+1 << ": " << N*(T-1) << endl;
    }

    return 0;
}
