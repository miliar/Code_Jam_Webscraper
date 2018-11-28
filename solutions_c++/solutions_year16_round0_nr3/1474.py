#include <bits/stdc++.h>
typedef long long ll;

using namespace std;
int T,J,N;
string toString(long long n){
	string s="";
	bool isNegative=(n<0);
	if(n==0){
		return "0";
	}
	if(n<0){
		n=n*-1;
	}
	while(n){
		int digit=n%10;
		n=n/10;
		s=char(digit+'0')+s;
	}
	if(isNegative){
		s="-"+s;
	}
	return s;
}

ll getNum2(ll num, int base){
	ll res=0;
	ll b=1;
	while(num){
		int dig = num%2;
		num/=2;
		res = res+ b*dig;
		b*=base;
	}
	return res;
}
string getNum(ll num){
	string ini = toString(getNum2(num,10));
	reverse(ini.begin(),ini.end());
	
	for(int j=ini.length();j<N-1;j++){
		ini.append("0");
	}
	ini.append("1");
	
	// reverse(ini.begin(),ini.end());
	return ini;
}

bool isDivsible(string& num, ll base, ll m){
	ll ans=0;
	ll b=1;
	for(int i=0;i<N;i++){
		ans= ans + (num[i]-'0')*b;
		ans=ans%m;
		b=(b*base)%m;
	}
	return ans==0;
}


vector<int> check(ll num){
	vector<int> v;
	string n=getNum(num);

	for(int i=2;i<11;i++){
		int ok=0;
		for(int j=2;j<100;j++){
			if(isDivsible(n,i,j) ){
				v.push_back(j);
				ok=1;
				break;
			}
		}
		if(ok==0){
			vector<int> vv;
			return vv;
		}
	}
	return v;
}
void doit(ll num){
	string n=getNum(num);

	for(int i=2;i<11;i++){
		for(int j=2;j<100;j++){
			if(isDivsible(n,i,j)){
				cout << j << " ";
				break;
			}
		}
		
	}
}
ll f(){
	ll start=1;
	int target = 0;
	vector<int> v;
	while(target<J){
		vector<int> vv=check(start);
		if(vv.size()!=0){
			v.push_back(start);
			target++;
		}
		start += 2;
	}

	for(int i=0;i<v.size();i++){
		string a1 = getNum(v[i]);
		reverse(a1.begin(),a1.end());
		cout << a1 << " ";
		doit(v[i]);
		cout << endl;
	}
}
int main(int argc, char const *argv[]){
	cout << "Case #1:" << endl;
	N=32;
	J=500;
	f();
	return 0;
}