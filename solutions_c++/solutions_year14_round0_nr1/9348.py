#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <cassert>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include <algorithm>
#define Pi 3.14159
#define vi vector<int>
#define pi pair<int,int>
#define si stack<int>

typedef long long int ll;
using namespace std;

int main ()
{
    ifstream inn;
    ofstream out;
    out.open("out.txt");
    inn.open("a.in");
    int test;
    inn>>test;
    for(int Z = 1; Z <= test;Z++)
    {
        int x;
        inn>>x;
        int A,b,c,d;
        int p,q,r,s;
        for(int i = 1; i <= 4;i++)
        {
            inn>>A>>b>>c>>d;
            if(i == x){p=A;q=b;r=c;s=d;}
        }
        int y;
        inn>>y;
        int u,v,w,z;
        for(int i = 1; i <= 4;i++)
        {
            inn>>A>>b>>c>>d;
            if(i == y){u=A;v=b;w=c;z=d;}
        }
        bool a[4] ={0};
        if(p == u || p == v|| p == w|| p == z)a[0]=1;
        if(q == u || q == v|| q == w|| q == z)a[1]=1;
        if(r == u || r == v|| r == w|| r == z)a[2]=1;
        if(s == u || s == v|| s == w|| s == z)a[3]=1;
        int count = 0 ;
        for(int i = 0 ;  i < 4;i++)if(a[i])count++;
        if(count == 0)
        {
            out<<"Case #"<<Z<<": Volunteer cheated!"<<endl;
            continue;
        }
        if(count > 1)
        {
          out<<"Case #"<<Z<<": Bad magician!"<<endl;
            continue;
        }
        if(a[0])out<<"Case #"<<Z<<": "<<p<<endl;
        if(a[1])out<<"Case #"<<Z<<": "<<q<<endl;
        if(a[2])out<<"Case #"<<Z<<": "<<r<<endl;
        if(a[3])out<<"Case #"<<Z<<": "<<s<<endl;
    }
}
