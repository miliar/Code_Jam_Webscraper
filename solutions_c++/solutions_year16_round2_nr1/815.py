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
 
int cnt[20];
map<int,string>m;
int ans[10];
int main(){
	int t,i,j;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	string s;
	m[0]="ZERO";
	m[1]="ONE";
	m[2]="TWO";
	m[3]="THREE";
	m[4]="FOUR";
	m[5]="FIVE";
	m[6]="SIX";
	m[7]="SEVEN";
	m[8]="EIGHT";
	m[9]="NINE";
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>s;
		for(i=0;i<s.length();i++){
			cnt[s[i]-'A']++;
		}
		int red=cnt['Z'-'A'];
		ans[0]=red;
		s=m[0];
		for(j=0;j<s.length();j++)
		cnt[s[j]-'A']-=red;
		
		red=cnt['X'-'A'];
		ans[6]=red;
		s=m[6];
		for(j=0;j<s.length();j++)
		cnt[s[j]-'A']-=red;
		
		red=cnt['G'-'A'];
		ans[8]=red;
		s=m[8];
		for(j=0;j<s.length();j++)
		cnt[s[j]-'A']-=red;
		
		red=cnt['W'-'A'];
		ans[2]=red;
		s=m[2];
		for(j=0;j<s.length();j++)
		cnt[s[j]-'A']-=red;
		
		red=cnt['U'-'A'];
		ans[4]=red;
		s=m[4];
		for(j=0;j<s.length();j++)
		cnt[s[j]-'A']-=red;
			
		red=cnt['O'-'A'];
		ans[1]=red;
		s=m[1];
		for(j=0;j<s.length();j++)
		cnt[s[j]-'A']-=red;
		
		red=cnt['T'-'A'];
		ans[3]=red;
		s=m[3];
		for(j=0;j<s.length();j++)
		cnt[s[j]-'A']-=red;
		
		red=cnt['F'-'A'];
		ans[5]=red;
		s=m[5];
		for(j=0;j<s.length();j++)
		cnt[s[j]-'A']-=red;
		
		red=cnt['S'-'A'];
		ans[7]=red;
		s=m[7];
		for(j=0;j<s.length();j++)
		cnt[s[j]-'A']-=red;
		
		red=cnt['N'-'A'];
		red/=2;
		ans[9]=red;
		s=m[9];
		for(j=0;j<s.length();j++)
		cnt[s[j]-'A']-=red;
		
		for(i=0;i<10;i++){
			for(j=0;j<ans[i];j++)
			cout<<i;
		}	
		cout<<endl;
		
	}
	fclose(stdout);
	return 0;
}
