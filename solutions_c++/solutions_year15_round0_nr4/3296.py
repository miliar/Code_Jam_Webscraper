#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int x,r,c;
	for(int it=1;it<=t;it++)
	{
		bool rq=false;
		cin>>x>>r>>c;
		if((r*c)%x!=0)rq=true;
		if(x>r && x>c)rq=true;
		if(x==3 && r*c==3)rq=true;
		if(x==4 && (r*c==8 || r*c==4))rq=true;
		cout<<"Case #"<<it<<": ";
		if(rq)cout<<"RICHARD"<<endl;
		else cout<<"GABRIEL"<<endl;
	}
	return 0;
}
