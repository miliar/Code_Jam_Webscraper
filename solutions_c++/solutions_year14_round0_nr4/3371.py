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
#define all(a) a.begin(),a.end()
using namespace std;

int main()
{
    int t;
    cin>>t;
    rep(looper,1,t+1)
    {
        int n;
        cin>>n;
        vector <int> naomi, ken;
        rep(i,0,n)
        {
            double in;
            cin>>in;
            naomi.push_back(in*pow(10,5));
        }
        rep(i,0,n)
        {
            double in;
            cin>>in;
            ken.push_back(in*pow(10,5));
        }
        sort(all(naomi));
        sort(all(ken));
        int l=0, r=0, war=0, dwar=0;
        rep(i,0,n)
        {
            if(naomi[i]>ken[l])
            {
                war++;
                l++;
            }
        }
        rep(i,0,n)
        {
            while(r<n && ken[r]<naomi[i])
                r++;
            if(r>=n)
                break;
            else
            {
                dwar++;
            }
            r++;
        }
        cout<<"Case #"<<looper<<": "<<war<<" "<<n-dwar<<endl;
    }
}
