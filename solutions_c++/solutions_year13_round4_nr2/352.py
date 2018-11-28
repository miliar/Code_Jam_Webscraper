#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;
#define For(i,n) for(int i=0;i<n;i++)
#define sz(i) int(i.size())
#define mst(i,n) memset(i,n,sizeof(i))
#define eps 1e-4
#define MOD 1000000007
#define LL long long
#define pi acos(-1)
#define ALL(n) n.begin(),n.end()
#define pb push_back
#define iFor(i,n) for(typeof(n.begin()) i=n.begin();i!=n.end();i++)

int main(){
	int ca,cc=0;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&ca);
	while(ca--){
        int n;
        LL p;
        cin>>n>>p;
        p--;
        LL mask = (1LL << n) - 1;
        LL rank = 0;
        LL t = 1;
        LL ans1 = 0;
        LL ans2 = 0;
        int cnt = 0;
        while(1){
            t <<= 1;
            if((1LL << n) - 1 - mask <= p) ans1 = rank;
            else break;
            rank += t;
            if(rank > (1LL << n) - 1)
                rank = (1LL << n) - 1;
            mask >>= 1;
            if(mask == 0 ){
                if(cnt++) break;
            }
        }
        mask = (1LL << n) - 1;
        rank = (1LL << n) - 1;
        t = 1;
        while(1){
            if(mask <= p) {
                ans2 = rank;
                break;
            }
            rank -= t;
            if(rank < 0)
                rank = 0;
            mask >>= 1;
            t <<= 1;
        }
        cout<<"Case #"<<++cc<<": "<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}
