#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll; 
typedef unsigned long long ull;
typedef pair<ll,ll> pll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<long long> vll;
ifstream fin("A-large.in");
ofstream fout("A-large.out");
#define cin fin
#define cout fout
string output(string s){
	string sub=s.substr(0,1);
	string word=sub;
	// cout<<sub<<endl<<word<<endl;
	for(int i=1;i<s.length();i++){
		// cout<<word<<endl;
		sub[0]=s[i];
		string a=sub+word;
		string b=word+sub;
		if(a>b){
			word=a;
		}
		else{
			word=b;
		}
	}
	return word;
}
int main(){
	int t;
	cin>>t;
	for(ll iter=1;iter<=t;iter++){
		string s;
		cin>>s;
		cout<<"Case #"<<iter<<": "<<output(s)<<endl;

	}


	return 0;
}
