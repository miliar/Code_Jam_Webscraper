#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

int main() {
	string G="GABRIEL";
	string R="RICHARD";
	int t;
	cin>>t;
	for (int cas = 1; cas <=t ; ++cas)
	{
		int x,r,c;
		cin>>x>>r>>c;
		string res;
		if(r*c<x)
			res=R;
		else if(x==1){
			res=G;
		}
		else if(x==2){
			if(r*c%2==0)
				res=G;
			else
				res=R;
		}
		else if(x==3){
			if(r*c%3==0 &&  (r*c)/3>1)
				res=G;
			else
				res=R;
		}
		else if(x==4){
			if(r*c==12 || r*c==16)
				res=G;
			else
				res=R;
		}
		cout<<"Case #"<<cas<<": "<<res<<endl;
	}
	return 0;
}