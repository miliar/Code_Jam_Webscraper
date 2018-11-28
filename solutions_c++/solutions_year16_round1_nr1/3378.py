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
	ll t,turn=1,num=0;
	cin>>t;
	while(t--){
		char str[1005];
		cin>>str;
		int len=strlen(str);
		cout<<"CASE #"<<turn<<": ";
		//cout<<str[0];
		char s[2010];
		int ind=1001,indl=1002;
		for(int i=0;i<len;i++){
			if(i==0)
			s[ind--]=str[i];
			else{
				if(str[i]>=s[ind+1])
				s[ind--]=str[i];
				else
				s[indl++]=str[i];
			}
		}
		for(int i=ind+1;i<=indl-1;i++)
		cout<<s[i];
		cout<<endl;
		
		
		turn++;
	}
}
