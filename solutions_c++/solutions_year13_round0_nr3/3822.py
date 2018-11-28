#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;
#define N 10000
#define MOD 1000000007
#define inf 1<<28
#define LL long long
#define abs(a) (a)<0?(-a):(a)
#define CLR(a) memset((a),0,sizeof((a)))
#define FRIN freopen("C-small-attempt0.in","r",stdin)
#define FROUT freopen("Csmall.txt","w",stdout)
bool is_palindrome(int x){
	int y[4],i=0,j,l=0;
	while(x){
		y[l++]=x%10;
		x/=10;
	}
	j=l-1;
	while(i<=j){
		if(y[i]!=y[j]) return false;
		i++;
		j--;
	}
	return true;
}
int main(){
	FRIN;
	FROUT;
	int test,i,j,k,ai[1003],no=0,a,b;
	for(i=1;i<10;i++) {
	   j=i*i;
	   if(is_palindrome(j)) ai[no++]=j;
	}
	ai[no++]=121;
	ai[no++]=484;
	//for(i=0;i<no;i++) printf("%d ",ai[i]);
	//cout<<endl;
	scanf("%d",&test);
	for(k=1;k<=test;k++){
		scanf("%d%d",&a,&b);
		j=0;
		for(i=0;i<no;i++){
			if(ai[i]>=a&&ai[i]<=b) j++;
			if(ai[i]>b) break;
		}
		printf("Case #%d: %d\n",k,j);
	}
	return 0;
}
