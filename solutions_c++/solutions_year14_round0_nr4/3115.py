#include <iostream>
#include <ctype.h>
#include <stack>
#include <queue>
#include <limits.h>
#include <fstream>
#include <map>
#include <cmath>
#include <ctime>
#include <cstring>
#include <algorithm>
#include <ctime>
#include <set>

#define rep(i, a) for(int i = 0; i < a; i++)
#define rep1(i, a) for(int i = 1; i <= a; i++)
#define fo(i, a, b) for(int i = a; i < b; i++)
#define defo(i, a, b) for(int i = a; i >= b; i--)
#define ll long long
#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a.size()))
#define x first
#define y second
#define SET(x, a) memset(x, a, sizeof(x));
using namespace std;

int main(){
    int test;
    int l = 0;
    freopen("a.in", "r", stdin);
    freopen("b.out", "w", stdout);
    cin>>test;

    while(test--){
        l++;
        double arr[1005],brr[1005];
        int n,i;
        cin>>n;
        for(i=0;i<n;i++){
            scanf("%lf",&arr[i]);
        }
        for(i=0;i<n;i++){
            scanf("%lf",&brr[i]);
        }
        sort(arr,arr+n);
        sort(brr,brr+n);
        int ans2 = 0,ans1 = 0;
        int it1 = 0,it2 = 0;
        while(it1<n){
            while(brr[it2]<=arr[it1]&&it2<n){
                it2++;
            }
            //cout<<it2<<"\n";
            if(it2>=n){
                break;
            }
            it2++;
            it1++;
            ans2++;
        }
        ans2 = n - ans2;
        it1 = 0;
        it2 = 0;
        while(it2<n){
            while(arr[it1]<=brr[it2]&&it1<n){
                it1++;
            }
            if(it1<n){
                ans1++;
                it1++;
            }
            if(it1==n){
                break;
            }
            it2++;
        }
        if(ans2<0){
            ans2 = 0;
        }
        cout<<"Case #"<<l<<": ";
        cout<<ans1<<" "<<ans2<<"\n";
    }
    return 0;
}
