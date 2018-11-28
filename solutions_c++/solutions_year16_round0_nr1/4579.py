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
ifstream fin("A-large.in");
ofstream fout("A-large.out");
#define cin fin
#define cout fout
map<int, int> myMap;
int accumilator(int n){
	int temp=n,vari;
	while(myMap.size()<10){
		vari=temp;
		while(vari>0){
			myMap[vari%10]++;
			vari/=10;
		}
		if(myMap.size()>=10){
			break;
		}
		else{
			temp+=n;
		}
	}
	return temp;

}
int main(){
	int t,n;
	cin>>t;
	for(int iter=1;iter<=t;iter++){
		cin>>n;
		myMap.clear();
		cout<<"Case #"<<iter<<": ";
		if(n>0){
			cout<<accumilator(n)<<endl;
		}
		else{
			cout<<"INSOMNIA"<<endl;
		}

	}
	return 0;

}