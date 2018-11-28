/*************************************************************
CodeJam 2016 - https://code.google.com/codejam/contest/6254486/dashboard
09/04/16
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

string temp = "00000000000000",s;
vector<string> radix;
vector<bool> isprime(200000001,true);
vll prime;

void initialize(){
	isprime[0] = isprime[1] = false;
	ford(i,2,isprime.size()-1){
		if(isprime[i]){
			prime.pb(i);
			for(int j=i ; j*i <= 200000000 ; ++j)
				isprime[j*i] = false;
		}
	}
	//for
}

void create_string(int n){
	if(n==0){
		s = "1" + temp;
		s = s + "1";
		radix.pb(s);
		return;
	}
	int index = 14 - n;
	ford(i,0,1){
		temp[index] = '0' + i;
		create_string(n-1);
	}
}


int main(int argc, char const *argv[])
{
	/* code */
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	initialize();
	create_string(14);
	long long test;
	cin>>test;
	ford(t,1,test){
		cout<<"Case #"<<t<<":\n";
		int n,j;
		cin>>n>>j;
		int ctr = 0;
		vll div(9);
		//cout<<radix.size()<<"\n";
		ford(i,0,radix.size()-1){
			if(ctr==50)
				break;
			bool flag = true;
			ford(j,2,10){
				ll num = 0;
				ford(k,0,15)
					num = num*j + (radix[i][k] == '1' ? 1 : 0 ) ;
			//	cout<<num<<" ";	
				if(num <= 200000000 && isprime[num]){
					flag = false;
					break;
				}
				bool flag2 = false;
				ll sq = sqrt(num);
				ford(k,2,sq)
					if(num%k == 0){
						div[j-2] = k;
						flag2 = true;
						break;
					}
				if(!flag2){
					flag = false;
					break;
				}	
			}
			if(flag){
				++ctr;
				cout<<radix[i];
				ford(j,0,8)
					cout<<" "<<div[j];
				cout<<"\n";
			}
			
		}
	}
	return 0;
}