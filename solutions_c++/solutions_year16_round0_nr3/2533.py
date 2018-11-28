/*
 * coin_jam.cpp
 * 
 * Created by: Ashik <ashik@KAI10>
 * Created on: 2016-04-09
 */


#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define mem(list, val) memset(list, (val), sizeof(list))
#define pb push_back

ll power[11][17];

void setPower()
{
	for(int i=1; i<11; i++) power[i][0]=1;
	for(int i=1; i<11; i++){
		for(int j=1; j<17; j++) power[i][j] = power[i][j-1]*i;
	}
}

ll isPrime(ll n)
{
	ll m = (ll)sqrt(n);
	for(ll i=2; i<=m; i++){
		if(n%i == 0) return i;
	}
	return 0;
}

const ll mask = 32768;

string transform(ll num)
{
	string ret="";
	while(num > 0){
		if(num&1) ret.pb('1');
		else ret.pb('0');
		
		num >>= 1;
	}
	return ret;
}

ll todec(ll b, string str)
{
	ll sum=0, count = 0;
	for(int i=str.size()-1; i>=0; i--){
		if(str[i] == '1') sum += power[b][count];
		count++;
	}
	return sum;
}

void print(string str)
{
	cout << str;
	for(int b=2; b<=10; b++){
		printf(" %lld", isPrime(todec(b, str)));
	}
	puts("");
}

int main()
{
	freopen("output", "w", stdout);

	/*int p,q,r;
	cin >> p >> q >> r;*/
	
	setPower();
	
	int count = 0;
	string str;
	
	puts("Case #1:");
	for(ll a = 32769; a<=65535 && count<50; a++){
		str = transform(a);
		if(a&1 && a&mask){
			
			bool ok = true;
			for(int b=2; b<=10; b++){
				ll div = isPrime(todec(b, str));
				if(!div){
					//printf("Base %d: divisor %lld\n", b, div);
					ok = false;
					break;
				}
			}
			
			if(ok){
				count++;
				print(str);
			}
		}
	}

	return 0;
}

