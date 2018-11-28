#include <iostream>
#include <cstring>
#include <stack>
#include <cstdio>
using namespace std;
#define LL long long
#define MOD 1000000007



int main() {
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 LL n;
 string s;
 int t;
 cin>>t;int cc=0;
 while(t--)
 {
 	cc++;
 	cin>>n;
 	cin>>s;
 	int i=0;
 	for(;i<=9;++i)
 	{
 		LL sum=i;
 		int fl=0;
 		for(int j=0;j<=n;++j)
 		{
 			if(sum<j){
 				fl=1;break;
 			}
 			sum+=s[j]-'0';
 		}
 		if(!fl)break;
 	}
 	cout<<"Case #"<<cc<<": "<<i<<"\n";
 }
 
    
  return 0;
}

