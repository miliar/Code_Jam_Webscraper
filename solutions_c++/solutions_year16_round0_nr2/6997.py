//
//  main.cpp
//  code_jam
//
//  Created by Yanzun Huang on 4/8/16.
//  Copyright © 2016 Yanzun Huang. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <string>
using namespace std;


int main()
{
    string t;
    string n;
    int num;
    getline(cin,t);
    num = stoi(t);
    for (int i = 1; i <= num; i++)
    {
        getline(cin,n);
        int* table = new int[n.length()];
        if (n[0] == '+')
        {
            table[0] = 0;
        }
        else
        {
            table[0] = 1;
        }
        for (int j = 1; j < n.length(); j++)
        {
            if (n[j] == '+')
            {
                table[j] = table[j - 1];
            }
            else if (n[j] != n[j - 1])
            {
                table[j] = table[j - 1] + 2;
            }
            else
            {
                table[j] = table[j - 1];
            }
        }
        cout<<"Case #"<<i<<": "<<table[n.length() - 1]<<endl;
        delete[] table;
    }
}