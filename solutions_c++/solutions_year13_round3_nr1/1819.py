//Coder Dange Laxmikant  

#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<set>
#include<map>
#include<utility>
#include<climits>
#include<sstream>

using namespace std;

#define S(a) scanf("%d",&(a))
#define SL(a) scanf("%lld",&(a))


 
int main(){
    long ans,n,c;
	int tc;
    string s;
    scanf("%d",&tc);
    for(int t=0;t<tc;t++)
	{
        ans=0;
        cin>>s;
        scanf("%ld",&n);
        for(long i=0;i<s.length();i++)
            for(long j=i+n;j<=s.length();j++){
                c=0;
                for(long k=i;k<j;k++)
                {
                    if(s[k]=='a' || s[k]=='e' || s[k]=='i'|| s[k]=='o' || s[k]=='u')
                        c=0;
                    else
                        c++;
                    if(c>=n){
                        ans++;
                        break;
                    }
                }
            }
 
        printf("Case #%d: %d\n",t,ans);
    }
}