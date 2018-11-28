#include<iostream>
#include<sstream>
#include<iomanip>
#include<stdlib.h>
#include<string>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<queue>
#include<stack>
#include<map>
#include<utility>
#include<algorithm>
#include<complex>
using namespace std;
#define loop(i,l,r) for(int (i)=(int)(l);(i)<(int)(r);(i)++)
#define rloop(i,l,r) for(int (i)=(int)(l);(i)>(int)(r);(i)--)
#define rep(i,n) loop(i,0,n)
#define rrep(i,n) rloop(i,n-1,-1)
#define INF 0x3f3f3f3f
#define mod 1000000007LL
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;
typedef complex<double> C;

vector<string> split(stringstream& ss){
	string str;
	vector<string> res;
	while(ss>>str)res.push_back(str);
	return res;
}

string solve(string s){
		string t,tmp; 
		rep(i,s.size()){
				if(t.size()==0){
						tmp=s[0];
						t.insert(0,tmp);
				}else{
						tmp=s[i];
						if(t[0]>s[i])t.insert(t.size(),tmp);
						else t.insert(0,tmp);
				}
		}
		return t;
}

int main(){
	int n;
	string s;
	cin>>n;
	rep(i,n){
			cin>>s;
			cout<<"Case #"<<i+1<<": "<<solve(s)<<endl;
	}
}

