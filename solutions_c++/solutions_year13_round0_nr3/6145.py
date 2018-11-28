#include<iostream>
using namespace std;

int ispal(int n){
	int x=n;
	int rn=0;
	int r=0;
	while(n!=0)
	{
		r=n%10;
		rn=rn*10+r;
		n=n/10;
	}
	
	//cout<<" x "<<x<<" rn "<<rn<<endl;
	
	return x==rn?1:0;
}

int issqr(int n){
	int i=1;
	while(i*i!=n){
		if(i*i>=n)
			break;
		i++;
	}
	if(i*i==n){
		if(ispal(i))
			return 1;
		return 0;
	}
	return 0;
}

int main()
{
	int tc;
	int a,b;
	int count;
	
	cin>>tc;
	
	for(int i=1;i<=tc;i++){		
		cin>>a>>b;
		count=0;
		for(int j=a;j<=b;j++){
			if(ispal(j)){
				if(issqr(j))
					count++;
			}
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}
