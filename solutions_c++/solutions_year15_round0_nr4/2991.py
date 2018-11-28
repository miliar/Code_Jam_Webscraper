#include<iostream>
#include<map>
#include<algorithm>
#include<math.h>
#include<stack>
#include<queue>
#include<string.h>
#include<vector>
#include<iomanip>
#include<cstdio>
#include<set>
#define REP(i,n)	for(int i=0;i<n;i++)
#define RE(i,j,n)	for(int i=j;i<n;i++)
using namespace std;
typedef long long LL;
typedef long L;
int main()
{
	//ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	REP(z,t)
	{
		int x,r,c;
		cin>>x>>r>>c;
		if(r>c)	swap(r,c);
		cout<<"Case #"<<z+1<<": ";
		int area=r*c;
		if(x==1)
		{
			
			cout<<"GABRIEL"<<endl;
			
		}
		else if(x==2)
		{
			if(r==1 && c==1)	cout<<"RICHARD"<<endl;
			else if(r==1 && c==2)	cout<<"GABRIEL"<<endl;
			else if(r==1 && c==3)	cout<<"RICHARD"<<endl;
			else if(r==1 && c==4)	cout<<"GABRIEL"<<endl;
			else if(r==2 && c==2)	cout<<"GABRIEL"<<endl;
			else if(r==2 && c==3)	cout<<"GABRIEL"<<endl;
			else if(r==2 && c==4)	cout<<"GABRIEL"<<endl;
			else if(r==3 && c==3)	cout<<"RICHARD"<<endl;
			else if(r==3 && c==4)	cout<<"GABRIEL"<<endl;
			else if(r==4 && c==4)	cout<<"GABRIEL"<<endl;
			//else cout<<"ELSE"<<endl;
		}
		else if(x==3)
		{
			if(r==1 && c==1)	cout<<"RICHARD"<<endl;
			else if(r==1 && c==2)	cout<<"RICHARD"<<endl;
			else if(r==1 && c==3)	cout<<"RICHARD"<<endl;
			else if(r==1 && c==4)	cout<<"RICHARD"<<endl;
			else if(r==2 && c==2)	cout<<"RICHARD"<<endl;
			else if(r==2 && c==3)	cout<<"GABRIEL"<<endl;
			else if(r==2 && c==4)	cout<<"RICHARD"<<endl;
			else if(r==3 && c==3)	cout<<"GABRIEL"<<endl;
			else if(r==3 && c==4)	cout<<"GABRIEL"<<endl;
			else if(r==4 && c==4)	cout<<"RICHARD"<<endl;
			//else cout<<"ELSE"<<endl;
		}
		else
		{
			if(r==1 && c==1)	cout<<"RICHARD"<<endl;
			else if(r==1 && c==2)	cout<<"RICHARD"<<endl;
			else if(r==1 && c==3)	cout<<"RICHARD"<<endl;
			else if(r==1 && c==4)	cout<<"RICHARD"<<endl;
			else if(r==2 && c==2)	cout<<"RICHARD"<<endl;
			else if(r==2 && c==3)	cout<<"RICHARD"<<endl;
			else if(r==2 && c==4)	cout<<"RICHARD"<<endl;
			else if(r==3 && c==3)	cout<<"RICHARD"<<endl;
			else if(r==3 && c==4)	cout<<"GABRIEL"<<endl;
			else if(r==4 && c==4)	cout<<"GABRIEL"<<endl;

		}
	}
	return 0;
}
