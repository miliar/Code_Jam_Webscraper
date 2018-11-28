#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;
unsigned int t, n, cnt, r, tmp, dig;
bool a[10];

int main() 
{
	_
	cin>>t;
	for(int tst=1; tst<=t; tst++)
	{
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<tst<<": "<<"INSOMNIA\n";
		}
		else
		{
			cnt=0;
			for(int i=0; i<=9; i++)
				a[i]=0;
			r=1;
			int last;
			while(cnt!=10)
			{
				tmp=n*r;
				last=tmp;
				dig;
				while (tmp != 0)
   				{
      				dig = tmp % 10;
      				if(a[dig]==0)
      				{
      					a[dig]=1;
      					cnt++;
      					if(cnt==10)
      					break;
      				}
      				tmp = tmp / 10;
   				}
   				r++;
			}
			cout<<"Case #"<<tst<<": "<<last<<endl;
				
		}
		
	}
	return 0;
}