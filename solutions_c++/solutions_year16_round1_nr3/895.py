/*************************************************************
CodeJam 2016 - https://code.google.com/codejam/contest/6254486/dashboard
16/04/16
Sahil Arora
*************************************************************/
#include<bits/stdc++.h>
using namespace std;

#define ll 			long long
#define vll 		vector< long long >
#define vvll 		vector< vll >
#define vd 			vector< double > 
#define ford(i,x,a) for(ll i=x;i<=a;++i)
#define fore(i,x,a) for(ll i=x;i>=a;--i)
#define pii pair<int,int>
#define pll pair<ll,ll>
#define mp make_pair
#define ff first
#define ss second
#define all(a) a.begin(), a.end()
#define pb push_back 
const ll mod = 1e9+7;

ll sz,a,x;
vll v(11),temp(12);

void make(int n){
	if(n==0){
		temp[0] = temp[a];
		temp[a+1] = temp[1];
		ford(i,1,a){
			if(v[temp[i]] != temp[i+1] && v[temp[i]]!=temp[i-1])
				return;
		}
		++x;
		return;
	}
	int ind = a - n + 1;
	ford(i,1,sz){
		bool flag = true;
		ford(j,1,ind-1)
			if(temp[j] == i){
				flag = false;
				break;
			}
		if(!flag)
			continue;
		temp[ind] = i;
		make(n-1);
	}
}

int main(int argc, char const *argv[])
{
	/* code */
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	long long test;
	cin>>test;
	ford(t,1,test){
		cout<<"Case #"<<t<<": ";
		ll mx=0;
		cin>>sz;
		ford(i,1,sz)
			cin>>v[i];
		ford(i,3,sz){
			a = i;
			x = 0;
			make(a);
			if(x>0)
				mx = i;
		}
		cout<<mx<<"\n";
	}
	return 0;
}
