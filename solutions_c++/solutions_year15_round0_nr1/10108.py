#include <bits/stdc++.h>
using namespace std;
#define max3(a, b, c) max(a, b) > max(b, c) ? max(a, b) : max(b, c)
#define min3(a, b, c) min(a, b) < min(b, c) ? min(a, b) : min(b, c)
#define digit(c) (c - '0')
#define SET( ARRAY , VALUE ) memset( ARRAY , VALUE , sizeof(ARRAY) )
#define Inf 2147483647
#define Pi acos(-1.0)
#define LL long long
#define F(i, a) for( int i = (0); i < (a); i++ )
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
int main(){
	int t,n,a,nop,sum,i,k=1;
	string s;
	scanf("%d",&t);
	while(t--){
		nop=0;sum=0;
		cin>>n;
		cin>>s;
		for(i=0;i<=n;i++){
			a=s[i]-'0';
			sum+=a;
			if(sum<(i+1)){
				nop=nop+i+1-sum;
				sum+=i+1-sum;
			}
		}
		printf("Case #%d: %d\n",k++,nop);
	}	
	return 0;;
}