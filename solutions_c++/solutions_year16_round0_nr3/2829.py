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

ll sieve[10000010]={0},primes[10000010],k=0,n,s,cnt=0;

void recur(ll nos[11],ll pos){
	if(pos == 0){
		ll i,j;
		for(i=2;i<=10;i++)
			nos[i] += 1;
		ll divs[11];
		for(i=2;i<=10;i++){
			bool flag = 0;
			for(j=0;j<k;j++){
				if(primes[j] >= nos[i])
					break;
				if(nos[i]%primes[j] == 0){
//					cout<<nos[i]<<" "<<primes[j]<<"\n";
					divs[i] = primes[j];
					flag = 1;
					break;
				}
			}
			if(flag == 0){
				for(i=2;i<=10;i++)
					nos[i]--;
				return;
			}
		}
		if(i == 11){
			cnt++;
			cout<<nos[10]<<" ";
			for(i=2;i<=10;i++)
				cout<<divs[i]<<" ";
			cout<<"\n";
			if(cnt == s)
				exit(0);
		}
		for(i=2;i<=10;i++)
			nos[i] -= 1;
		return;
	}
	ll temp[11];
	
	for(ll i=2;i<=10;i++)
		temp[i] = nos[i];
	recur(temp,pos-1);
	for(ll i=2;i<=10;i++)
		temp[i] += pow(i,pos);
	recur(temp,pos-1);
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);
	
	for(ll i=2;i<=1000000;i++){
		if(sieve[i] == 0)
			for(ll j=2;i*j<=1000000;j++){
				sieve[i*j] = 1;
			}
	}
	for(ll i=2;i<=1000000;i++){
		if(sieve[i] == 0)
			primes[k++] = i;
	}
	
	ll tc;
	cin>>tc;
	cin>>n>>s;
	ll temp[11];
	for(ll i=2;i<=10;i++)
		temp[i] = pow(i,n-1);
	cout<<"Case #1:\n";
	
	recur(temp,n-2);
	
	return 0;
}

