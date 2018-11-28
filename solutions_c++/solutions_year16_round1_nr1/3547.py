#include <cstdio>
#include<algorithm>
#include <cstring>
#include<iostream>
#include<cmath>
#include<set>
#include<iomanip>
#include<vector>
#include<map>

#define MOD 1000000007
#define inf 1009999999999999999
#define ninf -1009999999999999999
using namespace std;
typedef long long int ll;
		
long long powee(long long int ax, long long int b)
{
	if(b==1)
	return ax;
	else if(b==0)
	return 1;
	if(ax==1)
	return 1;
    long long x=1,y=ax; 
    while(b > 0)
    {
        if(b%2 == 1)
        {
            x=(x*y);
            if(x>MOD) x%=MOD;
        }
        y = (y*y);
        if(y>MOD) y%=MOD; 
        b /= 2;
    }
    return x;
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    long long int test,looper,j;
    scanf("%lld",&test);
    long long int  jhingalala=test;
    for(looper=0;looper<test;looper++)
    {
        string s,str;
        cin>>s;
        for(j=0;j<s.length();j++)
        {   
            if(j==0)
                str=str+s[j];
            else
            {
                if(s[j]>=str[0])
                    str=s[j]+str;
                else
                    str=str+s[j];
            }
        }
        cout<<"Case #"<<looper+1<<": "<<str;
        if(jhingalala-looper+1)
        printf("\n");
    }
    return 0;
}
