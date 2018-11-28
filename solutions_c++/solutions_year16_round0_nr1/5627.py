//never give up  try to code every time
#include<bits/stdc++.h>
#define s(a) scanf("%d",&a)
#define S(a)  scanf("%lld",&a)
#define p(a) puts("a")
#define loop(a) for(int i=0;i<a;i++)
#define mx(x,y) x>y?x:y
#define mn(x,y) x>y?y:x
#define lld long long
#define ld long
#define mod 1000000007
#define max 100005
#define pb(a)  push_back(a)
#define pp(a) pop_back(a)
#define code_lover int main
using namespace std;
code_lover()
{

    freopen("A-large.txt","r",stdin);
  //fclose (stdin);
	freopen("bbb.txt","w",stdout);
  int t;
   cin>>t;
for(int s=1;s<=t;s++)
{int arr[10]={0};
	lld n,p;
	cin>>n;

	if(2*n==0)
	   printf("Case #%d: INSOMNIA\n",s);
	   else
	   {lld j=1,ans,flag=0;
	   	while(flag==0)
	   	{
	   	   p=j*n;
			  while(p>0)
			  {lld c=0;
			  	lld r=p%10;
			  	arr[r]=1;
			  	for(int k=0;k<10;k++)
			  	      if(arr[k]==1)
			  	         c++;
			  	if(c==10)
			  	   {
			  	   	  flag=1;
			  	   	  break;
					 }
					 //ans=p;
					 p/=10;
			  }
			  ans=j*n;
			  j++;


		   }
		   printf("Case #%d: %lld\n",s,ans);
	   }
}

return 0;
}

