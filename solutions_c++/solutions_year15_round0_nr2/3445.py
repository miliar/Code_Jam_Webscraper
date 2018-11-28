#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cstdio>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<cassert>
#include<iomanip>
#include<string>
#include<cstring>
#include<cctype>
#include<cmath>
 
using namespace std;
typedef long long ll;
#define FRN(i,n) for(ll i=0;i<(ll)n;i++)
#define FRMN(i,m,n) for(ll i=m;i<(ll)n;i++)
#define pb push_back
#define mp make_pair 
typedef  vector<ll> vi;
typedef  vector<vector<ll> > vvi;
typedef  vector<string> vs;
typedef  vector<double> vd;
typedef  pair<ll,ll> pi;
typedef  map<ll,ll> mii;
typedef  map<string,ll> msi;
typedef  map<ll,string> mis;
typedef  set<ll> si;
typedef  set<string> ss;

int A[10005];
int main(){
    int T,cas=0;
	freopen("B-large.in","r",stdin);
	freopen("largeOutput.txt","w",stdout);
    scanf("%d",&T);
    for(int cc=1;cc<=T;cc++){
        int maxi=-1,D;
        scanf("%d",&D);
        for(int i=1;i<=D;i++){
            scanf("%d",&A[i]);
            maxi=max(maxi,A[i]);
        }
        int res=maxi;
        for(int i=1;i<=maxi;i++){
            int curr=0;
	    int mx=-1; 
            for(int j=1;j<=D;j++){
                if(A[j]>i){
                    curr+=((A[j]/i)+((A[j]%i==0)?0:1))-1;
                    mx=max(mx,i);
                }
                else mx=max(mx,A[j]);
            }
            curr+=mx;
            if(curr<res)res=curr;
        }
        printf("Case #%d: %d\n",cc,res);
    }
    return 0;
}
