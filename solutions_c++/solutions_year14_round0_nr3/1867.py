/*
   @Author lion_IT
*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>

#define For(i,a,b) for(int i = int(a); i <= int(b); i++)
#define Ford(i,b,a) for(int i = int(b); i >= int(a); i--)
#define rep(i,n) for(int i = 0; i < int(n);i++)
#define fi first
#define se second
#define mp make_pair
#define pii pair<int, int>
#define VI vector<int>
#define pb push_back
typedef long long llint;
const int maxn = 2*1000+5;
using namespace std;
//-------------------------------------------------------------------------------//
    int n, id[maxn], px[maxn], py[maxn], x[maxn], y[maxn];

#define IN ""
#define OUT ""
bool Compare(int i, int j){
    return x[i]<x[j]?true:(x[i]>x[j]?false:y[i]<y[j]);
}
int gcd(int a, int b){
    if(b==0)return a;
    return gcd(b, a%b);
}
void Solve(){
    For(loop,1,2*n)id[loop] = loop;
    For(loop,1,2*n){
        For(i,1,2*n){
            x[i] = px[i] - px[loop];
            y[i] = py[i] - py[loop];
            int GCD = gcd(x[i],y[i]);
            if(GCD>0){
                if(x[i]<0||(x[i]==0&&y[i]<0))GCD*=-1;
                x[i]/=GCD;
                y[i]/=GCD;
            }
        }
        sort(id+1,id+2*n+1,Compare);
        int head;
        int a = loop <= n;
        int b = loop > n;
        For(i,2,2*n){
            if(x[id[i]]!=x[id[i-1]]||y[id[i]]!=y[id[i-1]]){
                head = i;
                a = loop <= n ;
                b = loop > n;
            }

            a += id[i] <= n;
            b += id[i] > n;
            if(a+b>2&&a*b>0){
                a = min(a, 2);
                b = 3-a;
                if(loop <= n)a--;else b--;
                cout<<loop<<" ";
                For(j,head,i){
                    if(a>0&&id[j]<=n)cout<<id[j]<<" ",a--;
                    if(b>0&&id[j]>n)cout<<id[j]<<" ",b--;
                }
                cout<<endl;
                return;
            }
        }
    }
    cout<<-1<<endl;
}
int main(){
    freopen(IN,"r",stdin);
    freopen(OUT,"w",stdout);
        scanf("%d",&n);
        For(i,1,2*n)scanf("%d%d",&px[i],&py[i]);
        Solve();
    return 0;
}
