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
	int t;
	freopen("B-large.txt","r",stdin);
	freopen("loveu.txt","w",stdout);
	scanf("%d\n", &t);
	for(int r=1;r<=t;r++)
	 {int ans=0;
	 	char s[1000];
	 //	cin>>s;
	    scanf("%s",s);
	    
	    vector<int>v;
	 	char ch=s[0];
	 	int f=0,i=0,j=0,k;
	 	 while(i<strlen(s))
	 	 {   //cout<<"j";
	 	 	if(s[i]=='-')
	 	 	{j=i;
	 	 	  for( k=i+1;s[k]!='\0';)
	 	 	  {
	 	 		if(s[k]==s[j])
	 	 		     k++;
	 	 		     else
	 	 		     {  
					   break;
					   }
				}
				v.pb(j),v.pb(k-1);
					   i=k;  
			  }
			  else
			  {
			      i++;
			  	
			  }
		  }
		 //int ans=0;
		 for(int i=0;i<v.size();i+=2)
		 {if(v[i]==0)
		    ans+=1;
		    else
		    ans+=2;
		 }
		 printf("Case #%d: %d\n",r,ans);
		    
		     
			 
			 
			 
}
return 0;
}

