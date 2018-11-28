//Author: Jaydeep
//
#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define mod 1000000007
#define vec vector<ll>
#define matrix vector<vector<ll> >
#define pritnf printf

template <typename T>
string NumberToString ( T Number )
{
	stringstream ss;
	ss << Number;
	return ss.str();
}


int main()
{
	ll t,i=0,j,k,x,y,z,count=0,p,flag=0,ans=0,sum=0,l,n,t1,flag1=1;

	string s;



	scanf("%lld",&t);

	for(t1=0;t1<t;t1++)
	{
	    scanf("%lld",&n);

        set<char> S;

	    flag1=0;

	    for(i=1;i<10000;i++)
	    {
	        p=i*n;

	        s=NumberToString(p);
	     //   cout << s << " ";

	        l=s.length();

	        for(j=0;j<l;j++)
	            S.insert(s[j]);

            //printf("'%lld'",S.count(0));

	        flag=1;
	        for(j=0;j<=9;j++)
	        {
	            if(S.find(j+'0')==S.end())
	            {
	               // printf("*%lld*",j);
	                flag=0;
	                break;

	            }
	        }

	        if(flag==1)
	        {
	            flag1=1;
	            break;

	        }


	    }

	    ans=p;

	    if(flag1==1)
	    printf("Case #%lld: %lld\n",t1+1,ans);
	    else
	       printf("Case #%lld: INSOMNIA\n",t1+1);





	}

	return 0;
}
