//	created : 16/04/09
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
	int n ;
	string s;
	cin>>n;
	rep(i,n){
		cin>>s;
		cout<<"Case #"<<i+1<<": ";
		bool state = false;
		int cnt = 0;
		rep(j,s.size()){
			if(s[j] == '-'){
				if(!state)cnt ++;
				state = true;
			}else{
				state = false;
			}
		}
		int ret = 0;
		if(s[0] == '-')cnt --,ret++;
		ret += cnt * 2;
		cout<<ret;
		cout<<endl;
	}
}
