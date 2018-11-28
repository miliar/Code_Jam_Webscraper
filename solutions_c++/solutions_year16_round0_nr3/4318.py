#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<vector>
#include<stack>
#define gc getchar_unlocked
using namespace std;
typedef long long int int64;
int64 v[100],N,J;
int64 getDiv(int64 n){
	int64 i,sq=sqrt(n)+1;
	sq=min(n,sq);
	for(i=2;i<=sq;i++){
		if(n%i==0)return i;
	}
	return -1;
}
int64 getBaseNum(int64 b){
	int64 i,pr=b,ans=1;
	//cout<<"bits :";for(i=0;i<N-2;i++)cout<<v[i];cout<<endl;
	for(i=0;i<N-2;i++){
		ans+=(v[i]*pr);
		pr*=b;
	}
	ans+=pr;
	return ans;
}

void setBits(int64 n){
	int64 k,i;
	for(i=0;i<N-2;i++){
		k=n%2;
		v[i]=k;
		n/=2;
	}
}

int main()
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int64 i,j,k,n,m,t,vl,dv,fl=0,cnt=1,ans;
cin>>t;
while(t--){
 	scanf("%lld %lld",&m,&n);N=m;
 	printf("Case #%lld:\n",cnt);
 	for(i=1;i<16384;i++){
 		setBits(i);
 		fl=0;
 		for(j=2;j<=10;j++){
 			vl=getBaseNum(j);
 			dv=getDiv(vl);
 			//cout<<"value: "<<vl<<" divisor:"<<dv<<endl;
 			if(dv!=-1)fl++;
 		}
 		if(fl==9){
 			cout<<"1";for(j=N-3;j>=0;j--)cout<<v[j];cout<<"1";
	 		for(j=2;j<=10;j++){
	 			vl=getBaseNum(j);
	 			dv=getDiv(vl);
	 			cout<<" "<<dv;
	 		}
	 		n--;
	 		cout<<endl;
 		}
 		if(n==0)break;
 	}
	cnt++;
}
return 0;
}

