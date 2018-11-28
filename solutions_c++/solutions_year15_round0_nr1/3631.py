#include<bits/stdc++.h>
using namespace std;
#define F(n) FO(i,n)
#define FO(i,n) FI(i,0,n)
#define FI(i,f,l) for(int i=(f),ei=(l);i<ei;i++)
const int ms=1e3;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;cin>>t;F(t){
        int s;
        char t[ms+1];
        cin>>s>>t;
        int x=0,r=0;
        for(int j=0;t[j];j++){
            if(r<j){
                x+=j-r;
                r+=j-r;
            }
            r+=t[j]-'0';
        }
        printf("Case #%i: %i\n",i+1,x);
    }
}
