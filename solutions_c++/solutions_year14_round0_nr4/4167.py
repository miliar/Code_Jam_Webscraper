#include <iostream>
#include<algorithm>
using namespace std;

int main() {
	int t,n,i,j,la,lb,ra,rb;
	float a[1001]={0},b[1001]={0},count1,count2,k=0;
	cin>>t;
	while(t--)
	{
	k++;
	count1=0;
	count2=0;
	cin>>n;
	for(i=1;i<=n;i++)
	cin>>a[i];
	for(i=1;i<=n;i++)
	cin>>b[i];
	sort(a+1,a+n+1);
	sort(b+1,b+n+1);

	la=1;ra=n;lb=1;rb=n;
	while(la<=ra)
	{
	if(a[ra]<b[rb])
	{
	la++;rb--;
	}
	else
	{
	ra--;rb--;count1++;
	}
	}
	la=1;ra=n;lb=1;rb=1;
while(lb<=n)
{
while(b[lb]<a[la] && lb<=n)
{
lb++;
}
if(lb>n)
break;
la++;lb++;
}
count2=ra-la+1;
cout<<"Case #"<<k<<": "<<count1<<" "<<count2<<endl;


	
	}
	return 0;
}