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

int calc(string s){
		int res=0;
		char t=s[0];
		loop(i,1,s.size()){
				if(s[i]!=t){
						res++;
						t=s[i];
				}
		}
		if(t=='-')res++;
		return res;
}		
		
int main(){
		int n;
		string s;
		cin>>n;
		rep(i,n){
				cin>>s;
				cout<<"Case #"<<i+1<<": "<<calc(s)<<endl;
		}
}
