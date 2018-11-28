#include<bits/stdc++.h>
#define rt rich=true
using namespace std;
int main()
{
	int t;
	cin>>t;
	int x,r,c;
	for(int it=1;it<=t;it++)
	{
		bool rich=false;
		cin>>x>>r>>c;
		if((r*c)%x!=0)rt;
		if(x>r && x>c)rt;
		if(x==3 && r*c==3)rt;
		if(x==4 && (r*c==8 || r*c==4))rt;
		cout<<"Case #"<<it<<": ";
		if(rich)cout<<"RICHARD"<<endl;
		else cout<<"GABRIEL"<<endl;
	}
	return 0;
}