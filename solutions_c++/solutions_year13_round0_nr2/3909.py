#include<iostream>

int main()
{
using namespace std;

int t,n,m,x,y,z,p,a[101][101],tempo,count1,count2;
cin>>t;

for(x=0;x<t;x++)
{

cin>>n>>m;
for(y=0;y<n;y++)
{
for(z=0;z<m;z++)
{
cin>>a[y][z];
//cout<<a[y][z]<<" ";
}
}

for(y=0;y<n;y++)
{
	for(z=0;z<m;z++)
	{
		tempo=a[y][z];
		count1=count2=1;
		for(p=0;p<m;p++)
		{
			if(a[y][p]>tempo)
			count1=0;
        }
        for(p=0;p<n;p++)
        {
			if(a[p][z]>tempo)
			count2=0;
		}
		
		if((!count1)&&(!count2))
		{
			
			cout<<"Case #"<<x+1<<": "<<"NO \n";
            goto label;
        }
     }
}

cout<<"Case #"<<x+1<<": "<<"YES \n";
label:
;
}
return 0;
}
