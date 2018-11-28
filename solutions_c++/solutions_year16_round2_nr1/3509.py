#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <numeric>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
#include <iomanip>
using namespace std;
#define ll         long long
#define ld         long double
#define pb         push_back
#define mp         make_pair
#define sz(x)      (int)(x.size())
#define lp(i,n)    for (int i=0; i<n ; ++i)
#define lp1(i,n)   for (i=1; i<=n; ++i)
#define lpa(i,a,b) for (i=a; i<=b; ++i)
#define lpd(i,n)   for (i=(n)-1; i>=0; --i)
#define lpd1(i,n)  for (i=n;     i>0 ; --i)
#define lpb(i,a,b) for (i=b; i>=a; --i)
#define amin(a,b)  a=min(a,b)
#define amax(a,b)  a=max(a,b)
#define all(s)     (s).begin(),(s).end()
#define fill(s,v)  memset(s,v,sizeof(s))
int main () {
    //freopen("input.txt", "r", stdin);         //freopen("output.txt", "w", stdout);
	freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.txt", "w", stdout);
	//freopen("A-large.in", "r", stdin);          freopen("A-large.txt", "w", stdout);

    int ti=0,tn=1;  char ds[10]; cin>>tn; //cout<<tn<<"\n";
    cin.getline(ds,10);  //uncomment this to start reading string - dummy read

    while(ti++ < tn){
            printf("Case #%d: ",ti);
        //declarations:**************************************************
            char s[2000];
            int a[26] = {};
            int cnt[10];

        //input:  *******************************************************
            cin.getline(s,2000);

        //Logic:  *******************************************************
            lp(i,strlen(s)){
                a[s[i]-65]++;
            }
            cnt[0] = a[25];
            cnt[2] = a[22];
            cnt[4] = a[20];
            cnt[6] = a[23];
            cnt[8] = a[6];

            cnt[5] = a[5] - cnt[4];
            cnt[7] = a[21] - cnt[5];
            cnt[3] = a[7]  - cnt[8];
            cnt[1] = a[14] - cnt[0] - cnt[2] - cnt[4];
            cnt[9] = a[8]  - cnt[5] - cnt[6] - cnt[8];




        //Output: *******************************************************
            lp(i,10){
                lp(j,cnt[i]){
                    printf("%d",i);
                }

            }

            printf("\n");
    }//end of one test case

    return 0;
}
