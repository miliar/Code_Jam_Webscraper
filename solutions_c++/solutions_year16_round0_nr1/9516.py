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

int match(int s){
		char str1[20];
		const int bufsize=20;
		const int roll=100;
		int d=0,res=-1;
		vector<int> v,cnt(10,0);
		rep(i,100)v.push_back(s*(i+1));
		rep(i,100){
				_itoa_s(v[i],str1,bufsize,10);
				rep(j,strlen(str1))cnt[str1[j]-'0']++;
				d=0;
				rep(j,10)if(cnt[j]>0)d++;
				if(d==10){
						res=v[i];
						break;
				}
		}
		return res;
}
		
int main(){
		int d,n,res;
		cin>>d;
		rep(i,d){
				cin>>n;
				res=match(n);
				cout<<"Case #"<<i+1<<": ";
				if(res>0)cout<<res<<endl;
				else cout<<"INSOMNIA"<<endl;
		}
}

