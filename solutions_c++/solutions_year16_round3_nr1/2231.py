//
//  main.cpp
//  PBM#1
//
//  Created by Zebo Li on 5/8/16.
//  Copyright © 2016 Zebo Li. All rights reserved.
//

#include<string>
#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string.h>
#include<memory.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<map>
#include<numeric>
#include<deque>
#include<set>
#include<functional>
#include<queue>


#define REP(i,n) for(int (i)=0; (i)<(int)(n);(i)++)
#define ALL(x) x.begin(), x.end()
#define SZ(x) (int)(x).size()
#define RIT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MSET(m,v) memset(m,v,sizeof(m))

using namespace std;
typedef vector<int> vi;
typedef pair<int,int>ii;
typedef vector<pair<int,int> >vpii;
typedef long long llint;

template<typename T> inline void find_min(T&x,T y){ if(y<x) x=y;}
template<typename T> inline void find_max(T&x,T y){ if(y>x) x=y;}

template<typename T>
void printInfo(T&x)
{
    cout<<x<<' ';
}

class ppls
{
public:
    int num;
    char name;
    ppls(int n,char c):num(n),name(c){}
    friend bool operator < (const ppls &G1,const ppls &G2)
    {
        return G1.num < G2.num;
    }
};

int main()
{
    int T;
    FILE *fin,*fout;
    fin = fopen("A-large.in","r");
    if(fin == NULL)
    {
        printf("Cannot open the file!");
        return(0);
    }
    fout = fopen("output","w");
    if(fout == NULL)
    {
        printf("Cannot open the file!");
        return(0);
    }
    fscanf(fin,"%d",&T);
    priority_queue<ppls> q;
    for(int k=1;k<=T;k++)
    {
        int N,sum=0;
        fscanf(fin,"%d",&N);
        REP(i,N)
        {
            int tmp;
            fscanf(fin,"%d",&tmp);
            q.push(ppls(tmp,(char)('A'+i)));
            sum += tmp;
        }
        fprintf(fout,"Case #%d:",k);
        while(q.size())
        {
            ppls v1 = q.top();
            q.pop();
            ppls v2 = q.top();
            if(v1.num>v2.num+1)
            {
                cout<<v1.name<<v1.name<<' ';
                fprintf(fout," %c%c",v1.name,v1.name);
                q.push(ppls(v1.num-2,v1.name));
                sum -= 2;
            }
            else if(v1.num==v2.num+1)
            {
                cout<<v1.name<<' ';
                fprintf(fout," %c",v1.name);
                q.push(ppls(v1.num-1,v1.name));
                sum -= 1;
            }
            else if(v1.num>1)
            {
                cout<<v1.name<<v2.name<<' ';
                fprintf(fout," %c%c",v1.name,v2.name);
                q.pop();
                q.push(ppls(v1.num-1,v1.name));
                q.push(ppls(v2.num-1,v2.name));
                sum -= 2;
            }
            else if(sum == 3)
            {
                cout<<v1.name<<' ';
                fprintf(fout," %c",v1.name);
                sum -= 1;
            }
            else
            {
                cout<<v1.name<<v2.name<<' ';
                fprintf(fout," %c%c",v1.name,v2.name);
                q.pop();
                sum-=2;
            }
        }
        cout<<endl;
        fprintf(fout,"\n");
        
    }
    
    cout<<"Ilove Hyojung Kim forever!!\n";
}











