#include <bits/stdc++.h>
using namespace std;
 
#define MOD 1000000007
#define modulo(a) (a>0?a:-a)
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll; 
typedef unsigned long long ull;
typedef pair<ll,ll> pll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<long long> vll;
ifstream fin("B-large.in");
ofstream fout("B-large.out");
#define cin fin
#define cout fout

int main(){
	int t,n;
	cin>>t;
	string s;
	for(int iter=1;iter<=t;iter++){
		cin>>s;
		cout<<"Case #"<<iter<<": ";
		
		int inversions=0;
		for(int i=0;i<s.length()-1;i++){
			if(s[i]!=s[i+1]){
				
				inversions++;
			}
		}
		if(s[0]=='+'){
			cout<<(inversions+1)/2*2<<endl;
		}
		else{
			cout<<1+(inversions)/2*2<<endl;
		}
		


	}
	return 0;

}