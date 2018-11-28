#include<bits/stdc++.h>
using namespace std;

#define ll long
ll a=1000,b,c,i,j,l,n,m,k,q,t,x,y,z=1001,mnm,mxm;
char str[1001], ans[2001], start;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf(" %ld",&t);
    for(k=1; k<=t; k++) {
        scanf(" %s",&str);
        l=strlen(str);
        start=str[0];
        for(i=0; i<l; i++) {
        if(i==0) { ans[a]= str[0]; a--; }
        else if(str[i]>=start) {
            ans[a]=str[i];
            start=ans[a];
            a--;
        }
        else {
            ans[z]=str[i];
            z++;
        }
    }
    printf("Case #%d: ",k);
    for(int j=0; j<2001; j++) {
        if(ans[j]!=0) { cout<<ans[j];
        ans[j]=0;
        }
    }
    cout<<endl;
    }
    return 0;
}
