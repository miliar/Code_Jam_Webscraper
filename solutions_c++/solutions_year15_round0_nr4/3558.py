#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
	    string ans;
	   int x,r,c;
	   cin>>x>>r>>c;
	   
	    if(x==1) ans="GABRIEL";
	    else if(x==2 && ((r==1 && c==3) ||  (r==3 && c==1) || (r==1 && c==1) || (r==3 && c==3)) ) ans="RICHARD";
	    else if(x==2) ans="GABRIEL";
	    else if(x==3 && ((r>=3 && c>=2) ||(r>=2 &&c>=3)) && r*c%3==0) ans="GABRIEL";
	    else if(x==3) ans="RICHARD";
	    else if(x==4 && ( (r==4 && c==4) || (r==4 && c==3 ) || (r==3 && c==4) ) ) ans="GABRIEL";
	    else if(x==4) ans="RICHARD";
	    cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
