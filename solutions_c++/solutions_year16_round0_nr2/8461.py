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
#define MOD2 1000000007
#define BASE1 31
#define BASE2 255
#define MOD1 1000003
typedef unsigned long long int uint64;
typedef long long int int64;
 
 
int main(){
	int t,j;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	string s;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>s;
		int ans=0;
		for(int i=0;i<s.length();i++){
			if(s[i]=='-'){
				if(i)
				ans+=2;
				else
				ans+=1;
				for(j=i;j<s.length();j++){
					if(s[j]=='+')
					break;
				}
				i=j;
			}
		}
		cout<<ans<<endl;
	}
	fclose(stdout);
	return 0;
}
