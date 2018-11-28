#include<iostream>
#include<algorithm>

typedef long long ll;
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	ll t,n,i,m,j,k,digit,flag;
	ll seen[10];
	cin>>t;
	for(i=0;i<t;i++){

		cin>>n;

		for(j=0;j<10;j++){
			seen[j]=0;
		}

		cout<<"Case #"<<i+1<<": ";
		if(n==0){
			cout<<"INSOMNIA";
		}

		else{
			flag=1;

			for(j=1;;j++){
				m=j*n;
				
				do{
					digit=m%10;
					seen[digit]=1;
					m/=10;
				}while(m>0);

				for(k=0;k<10;k++){
					if(seen[k]==0){
						break;
					}
				}

				if(k==10)
					break;	

			}
			cout<<j*n;
		}
		cout<<endl;
	}
	return 0;
}