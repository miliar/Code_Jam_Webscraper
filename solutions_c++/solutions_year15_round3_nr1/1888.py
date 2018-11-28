#include<iostream>
#include<algorithm>
#include <bits/stdc++.h>
#define MOD 1000000007

using namespace std;

int main()
{
    freopen("shubham.in", "r", stdin);
    freopen("outputcode.txt", "w", stdout);
    long long int test,t,a,b,c,i,j,k,n,m,sum=0;
    cin >> test;
    for(i=0;i<test;i++)
    {
        cin >> a >> b >> c;
        if(b==c)
        	cout << "Case #" << i+1 << ": " << a-1+c << endl;
       	else if(c==1)
       		cout << "Case #" << i+1 << ": " << a*b << endl;
        else
        	cout << "Case #" << i+1 << ": " << (a*(b-1))/c+c << endl;
    }
}
