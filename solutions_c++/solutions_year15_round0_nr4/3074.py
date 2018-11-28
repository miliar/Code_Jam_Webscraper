#include <iostream>
using namespace std;

int main() {
	int n;
	cin>>n;
	for (int i=1;i<=n;i++)
	{
		
		cout<<"Case #"<<i<<": ";
		int a,b,c;
		cin>>a>>b>>c;
		if (a==1)
		cout<<"GABRIEL\n";
		if (c<b)
		{
		  int t=c;
		  c=b;
		  b=t;
		}
		if (a==2)
		{
		  if (b==2 || c==2 || c==4)
		  cout<<"GABRIEL\n";
		  else cout<<"RICHARD\n";
		}
		if (a==3)
		{
		  if (b==2&&c==3 || b==3)
		  cout<<"GABRIEL\n";
		  else cout<<"RICHARD\n";
		}
		if (a==4)
		{
		  if (b==3&&c==4 || b==4)
		  cout<<"GABRIEL\n";
		  else cout<<"RICHARD\n";
		}
	}
	return 0;
}
