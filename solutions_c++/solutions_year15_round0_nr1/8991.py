//Copyrights of the Code reserved with chetan_shukla

#include<bits/stdc++.h>
using namespace std;
char s[1005];
int main()
{
    //freopen("inp.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,j;
    cin>>t;
    for(j=1; j<=t; j++)
    {
    	int n,temp=0,ans=0,i,len,d;
    	cin>>n;
    	cin>>s;
    	len=strlen(s);
        int a[n+1];

        for(i=0; i<len; i++)
        {
            a[i] = s[i]-'0';
        }
    	d=a[0];
        for(i=1;i<=n;i++)
        {
            if(d>=i)
                d=d+a[i];
            else
            {
                ans=ans+(i-d);
                d=i+a[i];
            }
        }

    	printf("Case #%d: %d\n", j, ans);

    }

    return 0;
}
