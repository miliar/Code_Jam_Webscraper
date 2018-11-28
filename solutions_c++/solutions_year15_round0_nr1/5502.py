/********************

	root8950

*********************/


#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define PII pair<int,int>
#define ft first
#define sd second
#define MAXN MOD
#define mp make_pair
#define f_in(st) freopen(st,"r",stdin)
#define f_out(st) freopen(st,"w",stdout)
#define sc(x) scanf("%d",&x)
#define scll(x) scanf("%lld",&x)
#define pr(x) printf("%d\n",x)
#define prll(x) printf("%lld\n",x)
#define pb push_back
#define MOD 1000000007
#define MAX 900000
#define PIE 3.141592653589
#define inf INT_MAX/2
#define ASST(X,L,R) assert(X >= L && X <= R)

int idx=1;

bool check(int num,string str){
	bool flag=1;
	int l=str.length();
	for(int i=0;i<l;i++){
		if(num >= i){
			num+=str[i]-'0';
		}
		else flag=0;
	}
	return flag;
}

void solve(int low,int high,string str){
	int mid;
	while(low<=high){
		mid=(low+high)/2;
		if(check(mid,str)){
			if(check(mid-1,str)==0){
				break;
			}
			high=mid-1;
		}
		else{
			low=mid+1;
		}
	}
	cout << "Case #" << idx << ": ";
	idx++;
	cout << mid << "\n";
}

int main(){
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	int t;
	cin >> t;
	while(t--){
		int s;
		cin >> s;
		string str;
		cin >> str;
		solve(0,MAX,str);
	}
	return 0;
}
