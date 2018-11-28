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
	freopen("A-large.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	ll t,turn=1,num=1;
	cin>>t;
	while(t--){
		int n,isp=1,i=0,k;
		bool ispr[100];
		memset(ispr,false,sizeof(ispr));
		cin>>n;
		if(n==0)
		{
			cout<<"CASE #"<<turn<<": INSOMNIA"<<endl;
			turn++;
			continue;
		}
		while(isp){
			i++;
			num=n*i;
			while(num!=0){
				ispr[num%10]=true;
				num=num/10;
			}
			for(k=0;k<=9;k++)
			if(ispr[k]==false)
			break;
			if(k==10)
			isp=0;
			
		}
		cout<<"CASE #"<<turn<<": "<<n*i<<endl;
		turn++;
	}
}
