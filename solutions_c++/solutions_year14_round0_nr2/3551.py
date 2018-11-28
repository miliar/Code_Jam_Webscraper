#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <cmath>
#include <fstream>
#define si(i) scanf("%d",&i)
#define sl(i) scanf("%ld",&i)
#define sll(i) scanf("%lld",&i)
#ifndef ONLINE_JUDGE
    #define gc getchar
#else
    #define gc getchar_unlocked
#endif
#define ll long long
#define ull unsigned long long
#define rep(i,a,b) for(int i=a;i<b;i++)
#define repi(i,a,b) for(int i=a;i>b;i--)
#define MOD 1000000007
using namespace std;

int main()
{
    int t;
    cin>>t;
    rep(looper,1,t+1)
    {
        double c, f, x, time=0, temp, farm_time, current=2;
        cout.precision(7);
        cin>>c>>f>>x;
        start:
            temp=x/current;
            farm_time=c/current;
            if((x/(f+current)+farm_time)<temp)
            {
                time+=farm_time;
                current+=f;
                goto start;
            }
            else
            {
                time+=temp;
                cout<<"Case #"<<fixed<<looper<<": "<<time<<endl;
                continue;
            }
    }
    return 0;
}
