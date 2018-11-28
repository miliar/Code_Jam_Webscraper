#include<bits/stdc++.h>
#define ll long long int
#define P(n) printf("%lld",n)
#define Ps(n) printf("%s",n)
#define Pc(n) printf("%c",n)
#define PS() printf(" ")
#define Pn() printf("\n")
#define Sl(n) scanf("%lld",&n)
#define Si(n) scanf("%d",&n)
#define Sc(n) scanf("%c",&n)
#define Ss(n) scanf("%s",&n)
#define pb push_back
#define mp make_pair
#define pll pair< ll, ll >
#define repG(start,end,diff,var) for(var=start;var<end;var+=diff)
#define repL(start,end,diff,var) for(var=start;var>end;var-=diff)
#define TESTCASE ll t;Sl(t);while(t--)
#define mod (1000000000+7)
using namespace std;
 
#define gc getchar_unlocked
#ifndef ONLINE_JUDGE
#define gc getchar
#endif
 
ll get_num(){
    ll num = 0;
    char c = gc();
    ll flag = 0;
    while(!((c>='0' & c<='9') || c == '-'))
        c=gc();
    if(c == '-')
    {
        flag = 1;
        c=gc();
    }
    while(c>='0' && c<='9')
    {
        num = (num<<1)+(num<<3)+c-'0';
        c=gc();
    }
    if(flag==0)
        return num;
    else
        return -1*num;
}
 
ll i,j,k,l,n;
string s;

int main(){
	freopen("a.in","r",stdin);
	freopen("out.txt","w",stdout);
	l=0;
	TESTCASE{
		k=get_num();
		cin>>s;
		n=0;
		j=0;
		for(i=0;i<=k;i++){
			if(s[i]!='0'){
				if(j<i){
					n+=i-j;
					j=i+(s[i]-48);
				}
				else{
					j+=(s[i]-48);
				}
			}
		}
		cout<<"Case #"<<++l<<": "<<n<<endl;
	}
	
	return 0;
}
