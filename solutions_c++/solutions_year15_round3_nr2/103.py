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
#define MOD 1000000000
#define MAXN 500005
typedef unsigned long long int uint64;
typedef long long int int64;


string s1,s2;
int maxi,pay,cnt;
int k,l,s;
int valid[30];

int chck(string z){

int ret=0;
for(int i=0;i<z.length();i++){
	if(z[i]==s2[0]){
		int j;
		for(j=0;j<s2.length();j++){
			if(i+j>z.length())
			break;
			if(z[i+j]!=s2[j])
			break;
		}
		if(j==s2.length())
		ret++;
	}
}
return ret;
}


void go(string x,int le){
	if(le==s){
		cnt++;
		int val=chck(x);
		pay+=val;
		maxi=max(maxi,val);
		return;
	}
	for(int i=0;i<s1.length();i++){
			string ret=x;
			ret+=s1[i];
			go(ret,le+1);
	}
}
int main(){
	int t;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>k>>l>>s;
		cin>>s1>>s2;
		maxi=0;
		pay=0;
		cnt=0;
		string ret="";
		go(ret,0);
	//	cout<<" "<<maxi<<" "<<pay<<" "<<cnt<<endl;
		double ans=maxi;
		double sub=pay;
		sub*=1.0;
		sub/=cnt;
		ans-=sub;
		printf("%.7lf\n",ans);
	}
	fclose(stdout);
	return 0;
}
