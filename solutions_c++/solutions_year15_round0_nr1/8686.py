#include<iostream>
#include<cstdio>
using namespace std;
#include<stdlib.h>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("new.out","w",stdout);
	
	int t,i,sum,n,p,temp=0;
	char s[1005];
	cin>>t;
	while(temp!=t)
	{	
		sum=0;
		p=0;
		int x;
		cin>>n;
		for(i=0;i<=n;i++){
			cin>>s[i];
			}
		for(i=0;i<n;i++){
			sum=sum+(s[i]-'0');
			if((s[i+1]-'0')!=0){
				if(sum<(i+1)){
					x=((i+1)-sum);
					p=p+x;
					sum=sum+x;
				}
			}
		}
		cout<<"Case #"<<(temp+1)<<": "<<p<<endl;
		temp++;	
	} 
	
	//system("pause");
	return 0;
} 
