#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
#include <iomanip>
#include <cmath>
#include <iomanip>
#include <fstream>
#include <stdio.h>
#include <set>
#include <map>
#include <sstream>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
#define x first
#define y second
#define mp make_pair
#define pb push_back
ll G(ll a,ll b){if(b==0)return a;return G(b,a%b);}
int c[3],cnt;
vector<string> v;
string ss,t;
int n,r,p,s;
void f(){
	int q=1;
	bool flag=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<ss.length();j+=2*q){
			flag=0;
			for(int k=0;!flag && k<q;k++){
				if(ss[j+k]<ss[j+k+q]){
					flag=1;
				}
				else if(ss[j+k]>ss[j+k+q]){
					flag=1;
					for(int kk=0;kk<q;kk++)swap(ss[j+kk],ss[j+kk+q]);
				}
			}
		}
		q*=2;
	}
}
int main(){
	ios_base::sync_with_stdio(false);
	ifstream fin("A-large.in");
	ofstream fout("a.txt");
	int T;
	fin>>T;
	while(T--){
		v.clear();
		fin>>n>>r>>p>>s;
		ss="R",t="";
		c[0]=c[1]=c[2]=0;
		c[0]=1;
		for(int i=0;i<n;i++){
			for(int j=0;j<ss.length();j++){
				if(ss[j]=='R'){
					t+="RS";
					c[2]++;
				}
				else if(ss[j]=='P'){
					t+="PR";
					c[0]++;
				}
				else if(ss[j]=='S'){
					t+="PS";
					c[1]++;
				}
			}
			ss=t;
			t="";
		}
		f();
		if(c[0]==r && c[1]==p && c[2]==s)v.pb(ss);
		ss="P",t="";
		c[0]=c[1]=c[2]=0;
		c[1]=1;
		for(int i=0;i<n;i++){
			for(int j=0;j<ss.length();j++){
				if(ss[j]=='R'){
					t+="RS";
					c[2]++;
				}
				else if(ss[j]=='P'){
					t+="PR";
					c[0]++;
				}
				else if(ss[j]=='S'){
					t+="PS";
					c[1]++;
				}
			}
			ss=t;
			t="";
		}
		f();
		if(c[0]==r && c[1]==p && c[2]==s)v.pb(ss);
		ss="S",t="";
		c[0]=c[1]=c[2]=0;
		c[2]=1;
		for(int i=0;i<n;i++){
			for(int j=0;j<ss.length();j++){
				if(ss[j]=='R'){
					t+="RS";
					c[2]++;
				}
				else if(ss[j]=='P'){
					t+="PR";
					c[0]++;
				}
				else if(ss[j]=='S'){
					t+="PS";
					c[1]++;
				}
			}
			ss=t;
			t="";
		}
		f();
		if(c[0]==r && c[1]==p && c[2]==s)v.pb(ss);
		sort(v.begin(),v.end());
		fout<<"Case #"<<++cnt<<": ";
		if(v.size()==0)fout<<"IMPOSSIBLE\n";
		else fout<<v[0]<<"\n";
	}
}
