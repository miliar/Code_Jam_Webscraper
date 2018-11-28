#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(false);cin.tie(0);
using namespace std;
#define pb push_back
#define pob pop_back
#define pf push_front
#define pof pop_front
#define mp make_pair
#define all(a) a.begin(),a.end()
#define bitcnt(x) __builtin_popcountll(x)
#define MOD 1000000007
#define BASE1 31
#define BASE2 255
#define MOD1 1000003
typedef unsigned long long int uint64;
typedef long long int int64;
 
vector<int>ret;
void gen(int idx,int val,string s){
	if(idx==(int)s.length()){
		ret.pb(val);
		return;
	}
	if(s[idx]!='?'){
		int v=int(s[idx])-48;
		gen(idx+1,val*10+v,s);
		return;
	}
	for(int i=0;i<=9;i++){
		gen(idx+1,val*10+i,s);
	}
}

int main(){
	int t,i,j;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	string s,s1;
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>s>>s1;
		ret.clear();
		gen(0,0,s);
		vector<int>v=ret;
		ret.clear();
		gen(0,0,s1);
		vector<int>v1=ret;
		ret.clear();
		int diff=1e9,a1,a2;
		for(int i=0;i<v.size();i++){
			for(int j=0;j<v1.size();j++){
				int r1=v[i];
				int r2=v1[j];
				if(abs(r1-r2)<diff){
					diff=abs(r1-r2);
					a1=r1;
					a2=r2;
				}
				else if(abs(r1-r2)==diff){
					if(r1<a1){
						a1=r1;
						a2=r2;
					}
					if((r1==a1)&&(r2<a2)){
						a2=r2;
					}
				}
			}
		}
		diff=a1;
		int d=0;
		if(!diff)
		d++;
		int l=s.length();
		while(diff){
			d++;
			diff/=10;
		}
		while(d!=l){
			cout<<0;
			d++;
		}
		cout<<a1<<" ";
		diff=a2;
		d=0;
		if(!diff)
		d++;
		while(diff){
			d++;
			diff/=10;
		}
		while(d!=l){
			cout<<0;
			d++;
		}
		cout<<a2<<endl;
	}
	fclose(stdout);
	return 0;
}
