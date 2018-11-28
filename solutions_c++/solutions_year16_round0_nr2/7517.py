//Author: Jaydeep
//
#include<bits/stdc++.h>

using namespace std;

#define ll long long
#define mod 1000000007
#define vec vector<ll>
#define matrix vector<vector<ll> >
#define pritnf printf


char flip(char s)
{

    if(s=='+')
        return '-';
    return '+';

}


int main()
{
	int a[200005],t,i=0,j,k,x,y,z,count=0,p,flag=0,ans=0,sum=0,l,n,t1;

	char s[1005],c;


	scanf("%d",&t);

	for(t1=0;t1<t;t1++)
	{
	    scanf("%s",s);

	    count=0;

	    l=strlen(s);

	    while(1)
	    {
	        flag=1;

	        for(i=0;i<l;i++)
	        {
    	        if(s[i]!='+')
	            {
	                flag=0;
	                break;
	            }
	        }

	        if(flag==1)
	            break;
	    //    printf("hkjsg");
	        c=s[0];

	        for(i=0;i<l;i++)
	        {
	            if(s[i]==c)
	                s[i]=flip(s[i]);

	            else
	                break;

	        }

	        count++;


	    }


	    printf("Case #%d: %d\n",t1+1,count);

	}

	return 0;
}
