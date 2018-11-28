#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

bool isfair(long long num){
	if (num<10) return true;
	else{
		char c[999];
		int i=0;
		while (num>0){
			c[i++]=num%10;
			num/=10;
		}
		int j=0;
		while (j<=i/2){
			if (c[j]!=c[i-j-1]) return false;
			j++;
		}
		return true;
	}
}

int main()
{
	freopen("c:\\1.in","r",stdin);
	freopen("c:\\out1.txt","w",stdout);
	long long i;
	long long ans[100];
	int h=0;
	for (i=1;i<=10000000;i++){
		if(isfair(i)){
		if(isfair(i*i)) {ans[h++]=i*i;}
		}
	}
	
	int T;
	cin>>T;
	int ii;
	for(ii=1;ii<=T;ii++)
	{
		long long a,b;
		cin>>a>>b;
		int l=0;
		int sum=0;
		for (l=0;l<h;l++)
		{
			if(ans[l]>=a && ans[l]<=b){
				sum++;
			}
		}
			cout<<"Case #"<<ii<<": "<<sum<<endl;
			
	}
return 0;
}

