#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <map>
//cout.precision(0);
//cout.setf(ios_base::fixed)

using namespace std;
bool pal(int n)
{
	int h=0,m;
	m=n;
	while(n>9)
	{
		h=h*10+(n%10);
		n/=10;
	}
	h=h*10+n;
	//cout<<h<<"   "<<m<<endl;
	if(h==m)
		return 1;
	else
		return 0;
}

int main()
{
      freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	const int q=32;
	int t,cunt=1,c,a,b;
	cin>>t;
	int num[q];
	for(int i=1;i<q;i++)
		if(pal(i)&&pal(i*i))
		{
			num[i]=1;
			//cout<<i*i<<endl;
		}
		else
			num[i]=0;

	while(t--)
	{
		c=0;
		cin>>a>>b;
		for(int i=0;i<q;i++)
			if(i*i >=a && i*i<=b && num[i]==1)
				c++;


					
						cout<<"Case #"<<cunt++<<": "<<c<<endl;
		
	}
	return 0;
}
