#include<iostream>
#include<math.h>

using namespace std;

int main()
{int T,A,B,K,a1,b1,k1,num,count;
char a[10],b[10],k[10];
cin>>T;
	for(int l=0;l<T;l++)
	{cin>>A>>B>>K;a1=b1=0;count=0;num=0;
		
		for(int j=0;j<A;j++)
		for(int m=0;m<B;m++)
		{num=0;
		for(int i=0;i<10;i++)
		a[i]=b[i]=k[i]='0';
		a1=j;b1=m;
		
		for(int i=0;i<10;i++)
		{if((int)(a1%(2))){a[i]='1';}a1/=2;
		if((int)(b1%(2))){b[i]='1';}b1/=2;
		if('1'==b[i] && a[i]=='1')k[i]='1';}
		//cout<<a<<" "<<b<<" "<<k<<endl;
		for(int i=0;i<10;i++)
		if(k[i]=='1')num+=pow(2,i);
		
		if(num<K){count++;}
		//cout<<j<<" "<<m<<" "<<num<<endl;
		
		}
		
			cout<<"Case #"<<(l+1)<<": "<<count<<endl;	
		}
	
	return 0;
	}
