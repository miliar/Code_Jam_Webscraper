# include <bits/stdc++.h>
# define ll long long
# define MAX 1005
using namespace std ;
typedef pair <int ,int > ii ;
void inp(int &n){scanf("%d",&n);}
void print(int n){printf("%d\n",n);}

char s[MAX];
int main()
{
  int t,i,j,ans,n,total;
  inp(t);
  int c=0;
  while(t--)
  {
  	 c++;
  	 scanf("%d",&n);
  	 scanf("%s",s);
  	 
  	 total=0;
  	 ans=0;
  	 for(i=0;i<=n;i++)
  	 {
  	 
  	 	 if(i>total)
		   {
		   	  ans+=(i-total);
		   	  total=i;
		   } 
		
  	 	 total+=(s[i]-'0');
	 }
	 printf("Case #%d: %d\n",c,ans);
	 
  	 
  }

   return 0;
}

