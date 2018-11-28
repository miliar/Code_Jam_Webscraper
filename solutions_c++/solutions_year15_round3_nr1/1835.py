#include <bits/stdc++.h>
using namespace std;



int main() {
	freopen("A-small-attempt0 (1).in", "r", stdin);
  freopen("latest.out", "w", stdout);

	int t,i;
	cin>>t;
	for(i=1;i<=t;i++){

        int r,c,w,ans;
        cin>>r>>c>>w;
        ans = c/w;
        if(c%w!=0)
            ans+=1;
        ans+=w-1;

        ans=ans*r;

	      cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
