#include<iostream>
#include<algorithm>
#include<math.h>
#include<stack>
#include<limits.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<utility>
#include<map>
#include<vector>
#include<set>
#include<queue>
#include<deque>
#include<iterator>
#include <sstream>
#include <fstream>
using namespace std;
#define sci(n) scanf("%d",&n)
#define scl(n) scanf("%ld",&n)
#define scll(n) scanf("%lld",&n)
#define scs(a) scanf("%s",a)
#define pri(n) printf("%d",n)
#define prl(n) printf("%ld",n)
#define prll(n) printf("%lld",n)
#define pnl printf("\n")
#define pr_ printf(" ")
#define ll long long int
#define l long int
#define mp make_pair
#define re(i,n) for(i=0;i<n;i++)
#define repin(i,a,b) for(i=a;i>=b;i--)
#define rep(i,a,b) for(i=a;i<b;i++)
#define init(arr) memset(arr,0, sizeof(arr)) 
#define pairs pair<int,int>
#define fi first
#define se second
#define mod 1000000007
int main(){
	freopen("B-large.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	ll t,turn=1,num=1;
	cin>>t;
	while(t--){
		char str[150],pre;
		int flip=0;
		cin>>str;
		int len=strlen(str);
		if(str[0]=='+')
		pre='+';
		else
		pre='-';
		for(int i=1;i<len;i++){
			if(str[i]!=pre){
				flip++;
				pre=(pre=='+')?'-':'+';
			}
		}
		if(pre=='-')
		flip++;
		cout<<"CASE #"<<turn<<": "<<flip<<endl;
		turn++;
	}
}
