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
#define total 500005
#define M 1000000000001
#define NIL 0
#define EPS 1e-5
#define INF (1<<28)
typedef unsigned long long int uint64;
typedef long long int int64;
string s[110];
vector<string>v;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i;
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		cout<<"Case #"<<cas<<": ";
	int n,l=0,j;
	cin>>n;
	v.clear();
	//vector<string>v;
	int le[n];
	for(i=0;i<n;i++){
		cin>>s[i];
		le[i]=s[i].length();
		int j=1,prev=0;
		string x="";
		x+=s[i][0];
		while(j!=le[i]){
			if(s[i][j]==s[i][prev]){
				j++;	
			}
			else{
				x+=s[i][j];
				prev=j;
			}
		}	
		v.pb(x);
	//	cout<<x<<endl;
	}
	int ptr[n];
	for(i=1;i<n;i++){
		if(v[i]!=v[i-1])
		break;
		ptr[i]=0;
	}
	ptr[0]=0;
	if(i!=n){
		cout<<"Fegla Won"<<endl;
		continue;
	}
int ans=0;
while(1){
	vector<int>f;
	for(j=0;j<n;j++){
		int k=ptr[j];
		if(k>=le[j])
		continue;
		char x=s[j][ptr[j]];
		int l=0;
		while(s[j][k]==x){
		l++;
		k++;}
		f.pb(l);
		ptr[j]=k;
	}
	if(f.empty())
	break;
	sort(all(f));
	int mid=f[f.size()/2];
	for(i=0;i<f.size();i++)
	ans+=abs(mid-f[i]);
}
cout<<ans<<endl;}
fclose(stdout);
return 0;}
