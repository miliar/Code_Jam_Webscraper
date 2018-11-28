//
//  main.cpp
//  codejam1
//
//  Created by Virat Goyal on 09/04/16.
//  Copyright © 2016 Virat Goyal. All rights reserved.
//
#include <fstream>
#include <iostream>
#include <iostream>
#include <unordered_map>
using namespace std;
int main(int argc, const char * argv[]) {
    
    //long long int n= 100001;
   // int data;
    long long int n;
    
    ifstream infile;
    infile.open("input.txt");
    
    ofstream outfile;
    outfile.open("output.txt");
    long long int t;
    
    infile >> n;
    //cout<<n;
    int temp=0;
    while(n--)
    {
        temp++;
        infile>>t;
        if(t==0)
        {
            outfile<<"Case #"<<temp<<": INSOMNIA"<<endl;
            continue;
        }
        unordered_map<int,int> um;
        int count =0;
        long long int t_copy=t;
        while(count<10)
        {
            long long int num=t;
            while(num>0 && count<10)
            {
                int d= num%10;
                num=num/10;
                if(um[d]!=10)
                {
                    count++;
                    um[d]=10;
                }
            }
            t+=t_copy;
        }
        t-=t_copy;
        outfile<<"Case #"<<temp<<": "<<t<<endl;
        //cout<<"Case #"<<temp<<": "<<t<<endl;
    }
    outfile.close();
    infile.close();
    return 0;
}
