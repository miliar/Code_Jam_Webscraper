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

    int t,p=1; cin>>t;

    while(p<=t){

        int sm;cin>>sm;

        char arr[sm+1];

        cin>>arr;

        int sum=0,count=0;

        for(int i=0;i<sm+1;i++){

            int a = arr[i]-'0';

            if(sum<i){

                count+=i-sum;
                sum=i;
            }

            sum+=a;
        }

        cout<<"Case #"<<p<<": "<<count<<"\n";

        p++;
    }
}
