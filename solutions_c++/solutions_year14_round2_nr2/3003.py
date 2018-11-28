#define _CRT_SECURE_NO_WARNINGS
#include<bits/stdc++.h>



using namespace std;
int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	register int test,A,B,k,i,j,count=0,m=1;
	cin>>test;
	while(test--)
    {
        count=0;
        cin>>A;
        cin>>B;
        cin>>k;
        for(i=0;i<A;i++)
        {
            for(j=0;j<B;j++)
            {
                int t = i&j;
                   if(t<k)
                    count++;
            }
        }
        cout<<"Case #"<<m++<< ": ";
        cout<<count<<endl;
    }
	return 0;
}
