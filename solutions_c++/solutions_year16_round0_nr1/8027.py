#include<iostream>

using namespace std;

int checkem(int m[]){
	int sum=0;
	for(int i=0;i<10;i++)
		sum+=m[i];
	return sum;
}
void update(int m[],int n)
{
	
	while(n>0){
		m[n%10]=1;
		n=n/10;
	}
}

int main(){
	int t,j,n;
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int m[10]={};
		cin>>n;
		cout<<"Case #"<<(i+1)<<": ";
		if(n==0)
		{
			cout<<"INSOMNIA"<<endl;
		}
		else
		{
			update(m,n);
			for(j=1;checkem(m)!=10;j++)
				update(m,n*j);
			cout<<n*(j-1)<<endl;
		}
	}
	return 0;
}