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
#define PIE 3.141592653589
#define inf INT_MAX/2
#define ASST(X,L,R) assert(X >= L && X <= R)

int idx=1;

bool cmp(const int a,const int b){
	return a>b;
}

int solve(vector<int> &vec,int d){
	if(vec[0]==0 || vec[0]==1){
		return vec[0];
	}
	vector<int> vec1(d,0),vec2(d+1,0),vec3(d+1,0);
	for(int i=0;i<d;i++){
		if(vec[i]>=1){
			vec1[i]=vec[i]-1;
		}
		vec2[i]=vec[i];
		vec3[i]=vec[i];
	}
	vec2[0]=vec[0]/2;
	vec2[d]=ceil((float)vec[0]/2);
	if(vec[0]==9 || vec[0]==8){
		vec3[0]=3;
		vec3[d]=vec[0]-3;
		sort(vec2.begin(),vec2.end(),cmp);
		sort(vec3.begin(),vec3.end(),cmp);
		if( solve(vec2,d+1) > solve(vec3,d+1) ){
			return min(1 + solve(vec1,d) , 1 + solve(vec3,d+1));
		}
	}
	//cout << "vec2 " << vec2[0] <<  " vec3 " << vec3[0] << "\n";
	sort(vec2.begin(),vec2.end(),cmp);
	return min(1 + solve(vec1,d) , 1 + solve(vec2,d+1));
}

int main(){
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	int t;
	cin >> t;
	while(t--){
		int d;
		cin >> d;
		vector<int> p(d);
		for(int i=0;i<d;i++){
			cin >> p[i];
		}
		sort(p.begin(),p.end(),cmp);
		int ans=solve(p,d);
		cout << "Case #" << idx << ": ";
		idx++;
		cout << ans << "\n";
	}
	return 0;
}
