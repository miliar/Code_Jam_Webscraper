#include <bits/stdc++.h>
#define ull unsigned long long
#define ll long long
#define pii pair<int,int>
#define pb(x) push_back(x)
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define F(i,a,n) for(i=(a);i<(n);++i)
#define FD(i,a,n) for(i=(a);i>=(n);--i)
using namespace std;
int dp[10004][3][3][2];
int a[10005];
int mul[4][4];
int len;
int f(int ind,int part,int last,int sign)
{
	//cout<<ind<<" "<<part<<" "<<last<<" "<<sign<<endl;
	//getchar();
	if(ind==len){
		//cout<<"archit\n";
		//cout<<ind<<" "<<part<<" "<<last<<" "<<sign<<endl;
		if(part>2 && last==4 && sign==0)return 1;
		return 0;
	}
	
	int &res=dp[ind][part][last][sign];
	if(res!=-1)return res;

	int val;
	if(last==4)val=a[ind];
	else {
		val=mul[last][a[ind]];
		if(val<0){
			//cout<<last<<" "<<ind<<" "<<a[ind]<<" "<<val<<" change\n";
			val=-val;
			sign=1-sign;
		}
	}

	if(part<=2 && val==(part+1) && sign==0){
		res= f(ind+1,part,val,sign)|f(ind+1,part+1,4,0);
	} else {
		res= f(ind+1,part,val,sign);
	}
	return res;

}
int main()
{
	freopen("inp.in", "r", stdin);
     	freopen("out.txt", "w", stdout);
	
	mul[1][1]=-4;mul[1][2]=3;mul[1][3]=-2;
	mul[2][1]=-3;mul[2][2]=-4;mul[2][3]=1;
	mul[3][1]=2;mul[3][2]=-1;mul[3][3]=-4;

	int i,t,l,x;
	string s;
	cin>>t;
	int k=1;
	while(t--){
		cin>>l>>x>>s;
		len=l*x;

		F(i,0,l*x){
			a[i]=s[i%l]-'i'+1;
		}
	
		M(dp,-1);
		int ans=f(0,0,4,0);
		if(ans==0)cout<<"Case #"<<k++<<": NO"<<endl;
		else cout<<"Case #"<<k++<<": YES"<<endl;
	}
}
