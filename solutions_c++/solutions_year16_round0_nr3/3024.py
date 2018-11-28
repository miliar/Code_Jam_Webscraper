#include<bits/stdc++.h>
using namespace std;
long long int n,ab,z[1000001],x=1,y[100001];

	void fun()
	{
		long long int i=0,s=0,a,b,p=0,k;
		a=pow(2,n-1);
		b=pow(2,n)-1;
		for(int m=a;m<=b&&p<ab;m++){ i=0;n=m; if(m%2==0) continue;
		while(n!=0)
		{ y[i]=n%2;
		n/=2;
	i++;} for( k=2;k<=10;k++){s=0;x=1;
	for(long long int j=0;j<i;j++)
	{
	if(y[j]) s+=pow(k,j);	
	} z[k]=s; for(long long int v=2;v<=sqrt(z[k]);v++) {
		if(z[k]%v==0) { z[k]=v;x=0;
			break;
		} 
	} if(x==0) continue; else break; }   if(k==11){ p++;
	
	for(long long int w=i-1;w>=0;w--)
	cout<<y[w];
	cout<<" ";
	for(long long int w=2;w<=10;w++)
	{  cout<<z[w]<<" ";
	}
	} else continue; cout<<"\n";  continue;} 
	}
int main() {
long long int t,j,i;
cin>>t;
for(i=1;i<=t;i++)
{ 
	cin>>n>>j; ab=j;
	cout<<"Case #"<<i<<":"<<"\n";
		
	fun();
	cout<<"\n";
}
	return 0;
}