//	created : 16/04/16
// 	author   : Rp7rf
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <set>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
#define rep(i,a) for(int i = 0 ; i < a ; i ++)
#define loop(i,a,b) for(int i = a ; i < b ; i ++)
#define vi vector<int>
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define INF 1e9


int main(void){
	int n;
	string s;
	cin>>n;
	rep(i,n){
		cin>>s;
		cout<<"Case #"<<i+1<<": ";
	//	cout<<s<<endl<<endl;
		string ret = s.substr(0,1);
		loop(j,1,s.size()){
			if(ret[0] > s[j])ret += s[j];
			else ret = s[j] + ret;
		}
		cout<<ret<<endl;
	}
}
