//
//  main.cpp
//  standing ovation
//
//  Created by Yanqiao Zhan on 4/11/15.
//  Copyright (c) 2015 Yanqiao Zhan. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main(int argc, const char * argv[]) {
    int T;
    ifstream in("/Users/yanqiaozhan/Code/algorithmexercise/2015googlecodejam/A-large.in");
    ofstream out("/Users/yanqiaozhan/Code/algorithmexercise/2015googlecodejam/out");
  //  ifstream in("A-small-attempt3.in");
   // ofstream out("out");
    in>>T;
    for(int i=0;i<T;i++)
    {
        int sm;
        string person;
        int addition=0;
        int sum=0;
        in>>sm>>person;
        sum=person[0]-'0';
        for(int j=1;j<person.size();j++)
        {
            if(sum<j)
            {
                addition++;
                sum++;
            }
            sum+=person[j]-'0';
        }
        out<<"Case #"<<i+1<<": "<<addition<<endl;
    }
    return 0;
}
