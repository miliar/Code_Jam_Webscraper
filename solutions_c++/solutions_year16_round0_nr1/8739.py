#include <iostream>  
using namespace std;

int main()
{
int T,N,i,j,k;
cin>>T;
for(k=0;k<T;k++)
{
cin>>N;
i=1;
int num,temp,count=0,bucket[10],ans=0;
if(N==0) cout<<"Case #"<<k+1<<": INSOMNIA"<<endl;
else
{
	for(j=0;j<10;j++) bucket[j]=-1;
	while(1)
	{
		num=N*i;
		temp=num;
		while(temp)
		{
			if(count==10) break;
			if(bucket[temp%10]==-1) {bucket[temp%10]=temp%10;count++;}
			temp/=10;		
		}
		if(count==10) {ans=num;break;}
		i++;
	}
	cout<<"Case #"<<k+1<<": "<<ans<<endl;
}
}
return 0;
}
