//solution by Wsl_F
#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <bitset>
#include <numeric>
#include <cassert>
#include <time.h>
#include <ctime>
#include <memory.h>
#include <complex>
#include <utility>
#include <climits>
#include <cctype>
#include <x86intrin.h>



using namespace std;
#pragma comment(linker, "/STACK:1024000000,1024000000")


typedef long long LL;
typedef unsigned long long uLL;
typedef double dbl;
typedef vector<int> vi;
typedef vector<LL> vL;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef pair<LL,LL> pLL;

#define mp(x,y)  make_pair((x),(y))
#define pb(x)  push_back(x)
#define sqr(x) ((x)*(x))



void solve()
{
    LL sMax;
    cin>>sMax;
    string s;
    cin>>s;
    LL ans= 0;
    LL cur= 0;

    for (int i= 0; i<=sMax; i++)
    {
        if (i>cur) { ans+= i-cur; cur+= i-cur; }
        cur+= s[i]-'0';
    }
    cout<<ans<<endl;
}

int main()
{
 ios_base::sync_with_stdio(0);
 cin.tie(0);
 srand(__rdtsc());
 // LL a[110];
 // memset(a,0,sizeof(a));

 freopen("A-large.in","r",stdin);
 freopen("output.txt","w",stdout);
 //cout<<fixed;
 //cout<<setprecision(9);
 //cout<<(int)'a'<<" "<<(int)'A'<<endl;
 /*
 random_shuffle
random_device random_device;
mt19937 generator(random_device());
shuffle(v.begin(), v.end(), generator); string s;
*/

 int numberOfTestCases;
 cin>>numberOfTestCases;
 for (int testCase= 1; testCase<=numberOfTestCases; testCase++)
 {
    cout<<"Case #"<<testCase<<": ";
    solve();
 }
 return 0;
}


