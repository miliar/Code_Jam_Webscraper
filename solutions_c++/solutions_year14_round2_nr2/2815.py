#define _CRT_SECURE_NO_WARNINGS
#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	register int t,a,b,k,i,j,c=0,m=1;
	cin>>t;
	while(t--)
    {
        c=0;
        cin>>a;
        cin>>b;
        cin>>k;
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                int temp = i&j;
                   if(temp<k)
                    c++;
            }
        }
        cout<<"Case #"<<m++<< ": ";
        cout<<c<<endl;
    }

}
