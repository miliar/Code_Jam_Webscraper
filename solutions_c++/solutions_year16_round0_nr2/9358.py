//
//  main.cpp
//  GoogleCodeJam-Revenge of the Pancakes
//
//  Created by FANXUEZHOU on 16/4/9.
//  Copyright © 2016年 FANXUEZHOU. All rights reserved.
//
#include <iostream>
#include <string.h>
#include <cstring>
#include <vector>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <random>
#include <bitset>
#include <unordered_map>
#include <unordered_set>
#include <memory>
#include <list>
#include <fstream>
using namespace::std;
int step_add(string s);
string resever(string s)
{
    int length=(int)s.size();
    int i=0;
    int j=length-1;
    while(i<j)
    {
        char temp=s[i];
        s[i]=s[j];
        s[j]=temp;
        i++;
        j--;
    }
    for(i=0;i<length;i++)
    {
        if(s[i]=='+')
            s[i]='-';
        else
            s[i]='+';
    }
    return s;
}
int step_mins(string s)
{
    int length=(int)s.size();
    if(length==0)
        return 0;
    if(s[length-1]=='-')
        return step_mins(s.substr(0,length-1));
    if(s[0]==s[length-1])
    {
        int step1=1+step_add(s);
        s=resever(s);
        int step2=1+step_mins(s);
        return min(step1,step2);
    }
    else
    {
        int step1=1+step_add(s);
        s[0]='+';
        int step2=1+step_mins(s);
        return min(step1,step2);
    }
}
int step_add(string s)
{
    int length=(int)s.size();
    if(length==0)
        return 0;
    if(s[length-1]=='+')
        return step_add(s.substr(0,length-1));
    if(s[0]==s[length-1])
    {
        int step1=1+step_mins(s);
        s=resever(s);
        int step2=1+step_add(s);
        return min(step1,step2);
    }
    else
    {
        int step1=1+step_mins(s);
        s[0]='-';
        int step2=1+step_add(s);
        return min(step1,step2);
    }
}
int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    int t;
    ifstream infile;
    infile.open("B-small-attempt1.in");
    if(infile.fail())
    {
        cout <<"open fail!"<<endl;
        return -1;
    }
    string number;
    getline(infile,number);
    t=stoi(number);

    ofstream oufile;
    oufile.open("out.txt");
    for(int i=0;i<t;i++)
    {
        string s;
        getline(infile, s);
        cout << s<<endl;
        oufile << "Case #"<<i+1<<": ";
        cout <<"Case #"<<i+1<<": ";
        int x=step_add(s);
        oufile << x<<endl;
        cout << x <<endl;
    }
    infile.close();
    oufile.close();
    return 0;
}
