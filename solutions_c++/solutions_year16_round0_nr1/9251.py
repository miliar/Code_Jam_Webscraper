//
//  main.cpp
//  GoogleCodeJam-Counting Sheep
//
//  Created by FANXUEZHOU on 16/4/8.
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
//bool is_insomnia(uint64_t n)
//{
//    
//}
//void print_sheep(uint64_t n)
//{
//    if(n==0)
//    {
//        cout <<"INSOMNIA"<<endl;
//        return;
//    }
//    set<int> nums;
//    uint64_t single=n;
//    while(true)
//    {
//        uint64_t temp=n;
//        while(temp)
//        {
//            nums.insert(temp%10);
//            temp/=10;
//        }
//        if(nums.size()==10)
//        {
//            oufile <<n<<endl;
//            return;
//        }
//        else
//            n+=single;
//    }
//}
int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    int t;
    ifstream infile;
    infile.open("A-large.in");
    if(infile.fail())
    {
        cout <<"boggle.dat open fail!"<<endl;
        return -1;
    }
    string number;
    getline(infile,number);
    t=stoi(number);
    ofstream oufile;
    oufile.open("out.txt");

    for(int i=0;i<t;i++)
    {
        uint64_t temp;
        infile >>temp;
        oufile <<"Case #"<<i+1<<": ";
        if(temp==0)
        {
            oufile <<"INSOMNIA"<<endl;
            continue;
        }
        set<int> nums;
        uint64_t single=temp;
        while(true)
        {
            uint64_t tem=temp;
            while(tem)
            {
                nums.insert(tem%10);
                tem/=10;
            }
            if(nums.size()==10)
            {
                oufile <<temp<<endl;
                break;
            }
            else
                temp+=single;
        }

    }
    return 0;
}
