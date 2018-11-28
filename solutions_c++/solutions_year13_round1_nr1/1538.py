#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#define mod 1000000007
using namespace std;

int w,t,q,r,k,i;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	w=t;
	while(w--)
	{
		cin>>r>>k;
		for(i=r+1;;i+=2)
		{
			if(k-i*i+(i-1)*(i-1)>=0)
			{
				q++;
				k=k-i*i+(i-1)*(i-1);
			}
			else
			{
				break;
			}
		}
		cout<<"Case #"<<t-w<<": ";
		cout<<q<<endl;
		q=0;
	}
	return 0;
}
