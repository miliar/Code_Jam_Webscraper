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
	int t;
	int64 n,i;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>n;
		int64 pre=-1,ret;
		int dig[10]={0};
		
		for(i=1;;i++){
			ret=n*i;
			if(ret==pre)
			break;
			pre=ret;
			while(ret){
				dig[ret%10]=1;
				ret/=10;
			}
			ret=0;
			for(int j=0;j<=9;j++){
				if(dig[j])
				ret++;
			}
			if(ret==10)
			break;
		}
		if(ret==10)
		cout<<pre<<endl;
		else
		cout<<"INSOMNIA"<<endl;
	}
	fclose(stdout);
	return 0;
}
