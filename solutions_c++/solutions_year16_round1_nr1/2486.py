#include<bits/stdc++.h>
#define FOR(i,j,n) for(i=j;i<=n;i++)
#define si(n) scanf("%d",&n)
#define sl(n) cin>>n
#define pn(n) printf("%d\n",n)
#define ps(n) printf("%d ",n)
using namespace std;

int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
    int t,i,tt;si(t);
    string s,c,c1,c2;
    FOR(tt,1,t) {
    	cin>>s;
    	int n=s.size();
    	c1=c2="";
    	c="";
    	FOR(i,0,n-1) {
    		c1=s[i]+c;
    		c2=c+s[i];
    		if(c1>c2) c=c1;
    		else c=c2;
    	}
    	cout<<"Case #"<<tt<<": "<<c<<endl;
    }
	return 0;
}
