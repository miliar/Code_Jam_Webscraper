
#include<string.h>

#include<stdio.h>

#include<stdlib.h>

#include<ctype.h>

#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include<cstdlib>
#include <cstdio>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <utility>
#include <fstream>
#define INF     9999999
using namespace std;
double pp[30][1010][1010];
int main()
{
    ifstream cin("b.in");
    ofstream cout("out.out");
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        cout<<"Case #"<<tt<<": ";
        int a,b,k;
        cin>>a>>b>>k;
        long long num=0;
        for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            if((i&j)<k)num++;
           // cout<<i<<j<<(i&j)<<endl;
        }
        }
        cout<<num<<endl;
    }



}
