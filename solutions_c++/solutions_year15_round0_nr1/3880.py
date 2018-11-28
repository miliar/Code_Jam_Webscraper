

#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>
#include <queue>
//#include<bits/stdc++.h>

#define IN freopen("input.txt", "r", stdin);
#define OUT freopen("output.txt", "w", stdout);
#define clr(arr, key) memset(arr, key, sizeof arr)
#define pb push_back
#define mp(a, b) make_pair(a, b)
#define fs first
#define sc second
#define PI acos(-1)
#define CF ios_base::sync_with_stdio(0);
#define all(v) v.begin(), v.end()
#define no_of_ones __builtin_popcount // count 1's in a numbers binary representation
#define SZ(v) (int)(v.size())
#define eps 10e-7
#define oo (1LL<<60)
#define N 2010
#define mod 1000000007
#define re(i,a) for(int i=0; i<a; i++)
#define ll long long
#define pii pair<int,int>
#define llu unsigned long long int

//int row[8] = {0,1,1,1,0,-1,-1,-1};
//int col[8] = {-1,-1,0,1,1,1,0,-1};
//int row[4] = {0, 1, 0, -1};
//int col[4] = {-1, 0, 1, 0};
//int months[13] = {0, ,31,28,31,30,31,30,31,31,30,31,30,31};

using namespace std;

int main()
{
    IN
    OUT

    int T,n,csum[1010],ans,prev;
    string s;

    cin>>T;
    for(int cs=1; cs<=T; cs++)
    {
        cin>>n>>s;

        csum[0]=s[0]-'0';
        for(int i=1; i<=n; i++) csum[i]=csum[i-1]+s[i]-'0';
        ans=0;
        for(int i=0; i<=n; i++)
        {
            prev=csum[i]-(s[i]-'0');
//            cout<<i<<" "<<csum[i]<<" "<<t<<endl;
            if(s[i]!='0'&&prev+ans<i) ans+=(i-(prev+ans));
        }
        printf("Case #%d: %d\n",cs,ans);
    }
    return 0;
}


