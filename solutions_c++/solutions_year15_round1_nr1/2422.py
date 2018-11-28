///This  code is created by Samar Singh Holkar
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include<list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define sd(x) scanf("%d",&x)
#define sfd(x) scanf("%d",&x)
#define sfld(x) scanf("%lld",&x
#define pf printf

#define LL long long
#define ll long long
#define LD long double
#define ld long double
#define PB push_back
#define pb push_back
#define MP make_pair
#define mp make_pair
#define F first
#define S second

#define pii pair<int,int>
#define vi vector<int>
#define fr(i,n) for( int i=0; i<=n; i++)
#define frm(i,m,n) for(int i=m; i<=n; i++)
#define N 200000

int main(){

    int p=1,t; cin>>t;

    while(p<=t){

        int n; cin>>n;

        int arr[n];

        for(int i=0;i<n;i++){

            cin>>arr[i];
        }

        ll x=0,y=0;

        for(int i=1;i<n;i++){

            if(arr[i]<arr[i-1]) x+=(arr[i-1]-arr[i]);
        }

        int def=0;

        for(int i=1;i<n;i++){

            if(arr[i]<arr[i-1]) def = max(def,arr[i-1]-arr[i]);
        }

        for(int i=0;i<n-1;i++){

            y += min(def,arr[i]);
        }

        cout<<"Case #"<<p<<": "<<x<<" "<<y<<"\n";

        p++;
    }
}
