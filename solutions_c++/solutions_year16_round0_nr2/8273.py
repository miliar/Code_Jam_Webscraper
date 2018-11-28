#include<iostream>
#include<cmath>
#include<vector>
#include<iomanip>
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
typedef long long int lint;
#define loop(x,a,b) for(int x = a; x < b; x++)
int main()
{
	//your code here
	freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
	lint c=0,l=0,tc;
	cin>>tc;
	while(c<tc)
    {
        lint ans=0;
        string str;
        cin>>str;
        l=str.length();

        for(int i=l-1;i>=0;i--)
        {

            if(str[i]=='-')
            {
                ans++;
                for(int j=0;j<=i;j++)
                {

                    if(str[j]=='-')
                        str[j]='+';
                    else
                        str[j]='-';
                }
            }

        }
        cout<<"Case #"<<c+1<<": "<<ans<<endl;
     c++;
    }
	return(0);
}
