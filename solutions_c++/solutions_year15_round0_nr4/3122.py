#include<iostream>
using namespace std;
int main()
{
	int t,x,r,c;
	cin>>t;
	int i=0;
	while(t--)
	{
		i++;
		cin>>x>>r>>c;
		int s,l;
		int val = r * c;
		if(x>= 7 || val%x)
		{
		    cout<<"Case #"<<i<<": RICHARD"<<endl;
		    continue;
		}
		if(x == 3 || x== 4 || x== 5 || x == 6)
		{
			s = r < c ? r : c;
			l = r < c ? c : r;
			if( l >= x && s >= x-1)
		    		cout<<"Case #"<<i<<": GABRIEL"<<endl;
			else
		    		cout<<"Case #"<<i<<": RICHARD"<<endl;
			continue;
		}
		cout<<"Case #"<<i<<": GABRIEL"<<endl;
	}
	return 0;
}
