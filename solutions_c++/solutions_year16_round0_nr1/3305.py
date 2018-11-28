#include<bits/stdc++.h>
#define mod 1000000007
#include<bits/stdc++.h>
#define mod 1000000007
#define pp pair<ll,ll>
#define mp make_pair
#define ll long long
#define ff first
#define ss second
#define big 100000000000000000
using namespace std;

ll tc,t,n,i,cnt,num,temp;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);
	
	cin>>tc;
	for(t=1;t<=tc;t++){
		cin>>n;
		if(n == 0){
			cout<<"Case #"<<t<<": Insomnia\n";
			continue;
		}
		bool hsh[10] = {0};
		cnt = 0;i = 1;
		while(cnt < 10){
			num = n*i;
			i++;
			temp = num;
			while(temp){
				if(hsh[temp%10] == 0){
					hsh[temp%10] = 1;
					cnt++;
				}
				temp = temp/10;
			//	cout<<num<<"\n";
			}
		}
		cout<<"Case #"<<t<<": "<<num<<"\n";
	}
	return 0;
}

