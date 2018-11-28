//
//  main.cpp
//  GoogleCodeJam-Fractiles
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
uint64_t mypow(int64_t x,int64_t n)
{
    uint64_t prod=1;
    while (n)
    {
        if(n%2==1)
        {
            prod*=x;
        }
        x*=x;
        n/=2;
    }
    return prod;
}
void find_position(int k,int c,int s,ofstream &oufile)
{
    if((k-c+1)>s)
    {
        cout <<" IMPOSSIBLE"<<endl;
        oufile <<" IMPOSSIBLE"<<endl;
        return;
    }
    if((k-c+1)<=1)
    {
        uint64_t ans=1;
        for(int i=2;i<=k;i++)
        {
            ans=ans+mypow(k,c-i)*(i-1);
        }
        cout << " "<<ans<<endl;
        oufile << " "<<ans<<endl;
    }
    else
    {
        int n=k-c+1;
        for(int i=1;i<=n;i++)
        {
            uint64_t ans=1;
            for(int j=i;j<i+c;j++)
            {
                ans=ans+mypow(k,c-(j-i+1))*(j-1);
            }
            cout << " "<<ans;
            oufile << " "<<ans;
        }
        cout <<endl;
        oufile<<endl;
    }
}
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    int t;
    ifstream infile;
    infile.open("D-small-attempt2.in");
    if(infile.fail())
    {
        cout <<"open fail!"<<endl;
        //return -1;
    }
    string number;
    getline(infile,number);
    t=stoi(number);
    //t=1;
    ofstream oufile;
    oufile.open("out.txt");
    for(int i=0;i<t;i++)
    {
        string str;
        getline(infile, str);
        stringstream temp;
        temp << str;
        oufile << "Case #"<<i+1<<":";
        cout <<"Case #"<<i+1<<":";
        int k;//digit
        temp >>k;
        //k=4;
        int c;//round
        temp>>c;
        //c=3;
        int s;//people number
        temp >>s;
        //s=2;
        find_position(k, c, s,oufile);
        
    }
    infile.close();
    oufile.close();
    //cout << INT64_MAX<<endl;
    return 0;
}
