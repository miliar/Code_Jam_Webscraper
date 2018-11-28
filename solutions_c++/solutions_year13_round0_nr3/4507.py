//
//  main.cpp
//  Codejam
//
//  Created by Sorawit Suriyakarn on 4/13/13.
//  Copyright (c) 2013 Sorawit Suriyakarn. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

int t;
int x,y;
int p10[10];

map< int , int > M;

int prog()
{
    scanf("%d%d",&x,&y);
    int p = M.upper_bound( y )->second - M.lower_bound(x)->second;
    return p;
}

bool palin(int p)
{
    int x = p;
    int z = 0;
    while( x != 0 ) { x /= 10 ; z ++; }
    for(int c=0;c<z;c++)
    {
        // c vs z-c-1
        if( (p/p10[c])%10 != (p/p10[z-c-1])%10 ) return false;
    }
    return true;
}

int main(int argc, const char * argv[])
{
    //freopen("/Users/thepsint/Desktop/in.txt","r",stdin);
    freopen("/Users/thepsint/Desktop/out.txt","w",stdout);
    //printf("gg\n");
    
    p10[0] = 1;
    for(int c=1;c<10;c++) p10[c] = 10*p10[c-1];
    
    for(int c=1;c<=10000;c++) if( palin( c ) )
    {
        int r = c*c;
        if( palin( r ) ) M[r] = 0;
    }
    
    int k = 0;
    for(map<int,int>::iterator it=M.begin();it!=M.end();it++) it->second = ++k;
    
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        printf("Case #%d: ",c);
        printf("%d\n",prog());
    }

    return 0;
}

