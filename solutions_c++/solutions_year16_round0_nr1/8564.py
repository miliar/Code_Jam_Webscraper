#include<iostream>
using namespace std;
#define ll long long int

int main()
{
	int T;
	cin>>T;
	int cas=1;
	while(T--){
		int a[10]={0};
		ll N,M;
		int num,tot=0;
		cin>>N;
		if(N==0){
			cout<<"Case #"<<cas<<": "<<"INSOMNIA"<<endl;
			cas++;
			continue;
		}
		ll i=1;
		while(1){
			M = N*i;
			while(M!=0){
				num= M%10;
				a[num]++;
				if(a[num]==1) tot++;
				M/=10;
			}
			
			if(tot==10) break;
			i++;
		}
		cout<<"Case #"<<cas<<": "<<N*i<<endl;
		cas++;
	}

	return 0;
}
