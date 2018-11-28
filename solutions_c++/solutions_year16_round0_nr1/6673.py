#include <bits/stdc++.h>
using namespace std;

int checku(int a[])
{
    int i;
	for(i=0;i<10;i++){
		if(a[i]==0){
			return true;
		}
	}
	return false;
}

int main(void)
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

	int t,digit,i=1;
	long long int n,val,j;
	cin>>t;
	while(t--){
		int a[10]={0};
		cin>>n;
		j=1;
		val=n;
		if(n!=0){
			while(checku(a)){
				while(val>0){
					digit=val%10;
					a[digit]=1;
					val=val/10;
				}
				j++;
				val=j*n;
			}
		}
		if(n!=0)
			cout<<"Case #"<<i<<": "<<--j*n<<endl;
		else
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		i++;
	}
}
