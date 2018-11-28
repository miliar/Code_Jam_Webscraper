#include <stdio.h>
#include <iostream>

using namespace std;
int main()
{
//	FILE*f1=freopen ("w2.in", "r", stdin);
//	FILE*f2=freopen ("ouw2.txt", "w", stdout);
	int t,su,x,c,n,j,i;
  cin>>t;
  string s;
  for(su=1;su<=t;su++)
  {
	cin>>s;c=0;x=0;
	n=s.length();
	printf("Case #%d: ",su);
	for(i=0;i<n;i++)
	if(s[i]=='+')
	break;
	else
	x=1;
	if(x==1)
	c++;
	x=0;
	for(j=i;j<n;j++)
	{
	   if(s[j]=='+')
	   {
	      x=1;
	      
	   }
	   else
	   {
	     if(x==1)
	     { c+=2;x=0;
	     }
	   }
	}
	cout<<c<<endl;
  }
 return 0;
}
