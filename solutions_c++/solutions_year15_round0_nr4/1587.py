#include <iostream>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(0);
	int z;
	cin>>z;
	for(int x=1;x<=z;x++)
	{
		int n,r,c;
		bool p=0;
		cin>>n>>r>>c;
		if(n<7){
			if(((c%n ==0&&(r>=n-1) )||((r%n ==0)&&(c>=n-1) )))p=0;	
			else p=1;
		}
		else 
		{
			p=1;
		}
		if(p)cout<<"Case #"<<x<<": "<<"RICHARD"<<endl;
		else cout<<"Case #"<<x<<": "<<"GABRIEL"<<endl;
	}
}
