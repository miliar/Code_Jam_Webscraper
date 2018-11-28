#include<bits/stdc++.h>
using namespace std;
#define F(n) FO(i,n)
#define FO(i,n) FI(i,0,n)
#define FI(i,f,l) for(int i=(f),ei=(l);i<ei;i++)
const int pm=1e3;
int n,a[pm+1];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;cin>>t;F(t){
        int x=INT_MAX;
        cin>>n;
        fill(a,a+pm+1,0);
        F(n){int p;cin>>p;a[p]++;}
        for(int i=1;i<=pm;i++){
            int t=0;
            for(int j=i+1;j<=pm;j++)
                t+=a[j]*(j/i+(j%i?1:0)-1);
            x=min(x,i+t);
        }
        printf("Case #%i: %i\n",i+1,x);
    }
}
