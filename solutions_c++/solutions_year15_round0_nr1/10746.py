#include <iostream>

using namespace std;

int main () {
  
int t,n,i,j,x=1,max;
char a[6];
cin>>t;
while(t--)
{
	cin>>n;
	max=0;
	j=0;
	for(i=0;i<=n;i++)
	{ cin>>a[i];
		if(j<i)
		{
			if((i-j)>max)
			max=i-j;
		}
		j+=(int)a[i]-48;
		
	}
	cout<<"Case #"<<x++<<":"<<" "<<max<<"\n";
}
}