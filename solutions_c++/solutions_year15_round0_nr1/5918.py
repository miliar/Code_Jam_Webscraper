#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main()
{
   // freopen("A-small.in", "r", stdin);
   // freopen("A-small.out", "w", stdout);
    int T ,i,n,temp,ans;
	string s;
    cin>>T ;
    int cnt = 1;
    while(T--)
    {

		cin>>n>>s;
		int len=s.length();
		ans=0;
		temp=s[0]-48;
		for(i=1;i<len;++i)
		{
                 if( temp<i && s[i]!='0')
                 {
                 	ans=ans+(i-temp);
                 	temp=temp+(i-temp)+(s[i]-48);
                 }
                 else
                 	temp=temp+s[i]-48;
		}

            cout<<"Case #"<<cnt++<<": "<<ans<<endl ;

    }
    return 0 ;
}

