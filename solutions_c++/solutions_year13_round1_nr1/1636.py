#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<algorithm>
#include<cmath>
#include<math.h>
using namespace std;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out","w",stdout);
	int T,r,t;
	cin>>T;
	for(int CASE=1 ; CASE<=T ; CASE++)
	{
		cin>>r>>t;
		int counter=0;
		int i=r+1;
		while(t>0)
		{
			if(t-( (i*i) - ( (i-1)*(i-1) ) ) >=0 )
				counter++;
			t=t-( (i*i) - ( (i-1)*(i-1) ) );
			i+=2;
		}
		cout<<"Case #"<<CASE<<": "<<counter<<endl;
	}
	return 0;
}