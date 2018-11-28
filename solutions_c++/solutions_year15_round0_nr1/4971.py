//
//  main.cpp
//  CodeJam
//
//  Created by Mousic on 4/11/15.
//  Copyright (c) 2015 Mousic. All rights reserved.
//

//
//  main.cpp
//  CodeJam
//
//  Created by Mousic on 4/11/15.
//  Copyright (c) 2015 Mousic. All rights reserved.
//

//
//  main.cpp
//  CodeJam
//
//  Created by Mousic on 4/11/15.
//  Copyright (c) 2015 Mousic. All rights reserved.
//

//
//  main.cpp
//  CodeJam
//
//  Created by Mousic on 4/11/15.
//  Copyright (c) 2015 Mousic. All rights reserved.
//

#include<string>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<sstream>
#include<iostream>
#include<utility>
//#include<bitset>

using namespace std;

#define pi pair<int,int>
#define vi vector<int>
#define vpi vector<pi>
#define vd vector<double>
#define vs vector<string>
#define vsi vector<string>::iterator

#define fst first
#define snd second
#define pb push_back
#define SIZE(a) (int)(a.size())
#define LENGTH(a) (int)(a.length())
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n);i>=0;i--)
#define FOR(i,n,m) for(int i=(n);i<=(m);i++)
#define FORD(i,n,m) for(int i=(n);i>=(m);i--)
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define MIN3(a,b,c) MIN( MIN(a,b),MIN(a,c) )
#define MAX3(a,b,c) MAX( MAX(a,b),MAX(a,c) )
#define ABS(a) ( (a)<0 ? -(a) : (a))
#define STRUMIEN(A,B) istringstream A(B)
#define SORT(A) sort(A.begin(),A.end())

////////////////////////////////////////////////////////////////////////////////
int T,n0,n1,n2,n3,sum;
string s1,s2,s3;
int rs;

int main()
{
    cin>>T;
    REP(i,T) {
        cin >> n1 >> s1;
        int sum(0),n0(0),rs(0);
        
        REP(j, n1+1) {
            n0 = atoi(s1.substr(j,1).c_str());
            //sum += n0;
            if (j==0 && n0==0) {
                rs = 1;
                sum = 1;
            } else if(sum<j) {
                rs += 1;
                sum = j+n0;
            } else {
                sum += n0;
            }
        }
        
        cout << "Case #" << i+1 << ": " << rs <<endl;
    }
    return 0;
}

