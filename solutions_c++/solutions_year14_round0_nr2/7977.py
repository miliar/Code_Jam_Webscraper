#include <iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int main() {
	freopen("B-large.in","rt",stdin);
	freopen("output.txt","wt",stdout);
	
int t;
cin>>t;
int q=0;
while(t--)
{
	q++;
cout<<"Case #"<<q<<": ";
	double c,f,x,ans,i=0,j,a,b,t2,t1;
	cin>>a>>f>>x;
	ans=0;
	c=0;
	
	
	while(i!=1)
	{
		t1=x/(f*c+2);
		t2=a/(f*c+2)+x/((f*c)+f+2);
		if(t2>=t1)
		{
			i=1;
			ans+=t1;
			break;
		}
		
		ans+=a/((f*c)+2);
		c++;
		
	}
	
	printf("%.7lf\n",ans);
}




	return 0;
}
