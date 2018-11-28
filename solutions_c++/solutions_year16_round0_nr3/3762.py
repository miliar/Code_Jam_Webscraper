//
//  coin_jam_opt.cpp
//  CodeJam_2016
//
//  Created by Snehil Vishwakarma on 4/9/16.
//  Copyright © 2016 Indiana University Bloomington. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>

using namespace std;

int J,N;
ofstream f2;

long prime_checker(vector<int> num,int base)
{
    long i;
    bool chk=false;
    long v=1+pow(base,N-1);
    for(i=0;i<num.size();i++)
        v+=pow(base,num[i]);
    if(v%2==0)
        return 0;
    //cout<<"Base: "<<base<<" Number: "<<v<<"\n";
    for(i=3;i<=(sqrt(v)+1);i=i+2)
    {
        if(v%i==0)
        {
            chk=true;
            break;
        }
    }
    if(chk)
        return i;
    else
        return 0;
}

void mult_recur(vector<int> num,int k)
{
    if(k==N-1 && J>0)
    {
        int i,r;
        long v;
        long *tval=new long[9];
        for(i=2;i<=10;i++)
        {
            tval[i-2]=prime_checker(num,i);
            if(!tval[i-2])
                break;
        }
        if(i==11)
        {
            v=1+pow(10,N-1);
            for(r=0;r<num.size();r++)
                v+=pow(10,num[r]);
            f2<<v;
            for(i=0;i<9;i++)
                f2<<" "<<tval[i];
            f2<<endl;
            J--;
        }
    }
    else if(J>0)
    {
        mult_recur(num,k+1);
        num.push_back(k);
        mult_recur(num,k+1);
        num.pop_back();
    }
}

int main()
{
    ifstream f1;
    f1.open("IS3_2016.in");
    f2.open("OS3_2016.out");
    
    int T;
    f1>>T;
    int i;
    vector<int> num;
    for(i=0;i<T;i++)
    {
        f1>>N>>J;
        num.clear();
        f2<<"Case #"<<(i+1)<<":\n";
        mult_recur(num,1);
    }
    f1.close();
    f2.close();
    return 0;
}