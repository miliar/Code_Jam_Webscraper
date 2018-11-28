#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;

int main()
{
	FILE*f1=freopen ("c2.in", "r", stdin);
FILE*f2=freopen ("rr.txt", "w", stdout);
  int t,si,i,j,s[30],count[30],n;
  cin>>t;
  for(si=1;si<=t;si++)
  {
  string a;
  cin>>a;
  n=a.size();
  for(i=0;i<27;i++)
  count[i]=0,s[i]=0;
   for(i=0;i<n;i++)
   {
	   count[a[i]- 'A'+1]++;
	   
   }
  // for(i=0;i<27;i++)
   //cout<<count[i]<<" ";
   for(i=0;i<n;i++)
   {
	   
	   if(count[26]>0&&count[5]>0&&count[18]>0&&count[15]>0)
	   {
		   s[0]++;
		   count[26]--;count[5]--;count[18]--;count[15]--;
		   }
	   
		else if(count[20]>0&&count[23]>0&&count[15]>0)
		{
			s[2]++;count[20]--;count[23]--;count[15]--;
			}
		   
		else if(count[6]>0&&count[15]>0&&count[18]>0&&count[21]>0)
		{
			 s[4]++;
			 count[6]--;count[15]--;count[18]--;count[21]--;
		}
		else if(count[6]>0&&count[9]>0&&count[22]&&count[5]>0)
		{
			s[5]++;
			count[6]--;count[9]--;count[22]--;count[5]--;
			}
		else if(count[19]>0&&count[9]>0&&count[24]>0)
		{
			s[6]++;
			count[19]--;count[9]--;count[24]--;
		}
		
		else if(count[5]>0&&count[9]>0&&count[7]>0&&count[8]>0&&count[20]>0)
		{
			s[8]++;
			count[5]--;count[9]--;count[7]--;count[8]--;count[20]--;
		}
		else if(count[20]>0&&count[8]>0&&count[18]>0&&count[5]>1)
		{
			s[3]++;
			count[20]--;count[8]--;count[18]--;count[5]-=2;
		}	
		else if(count[14]>1&&count[9]>0&&count[5]>0)
		{
			s[9]++;
			count[14]-=2;count[9]--;count[5]--;
			}
			else if(count[15]>0&&count[14]>0&&count[5]>0)
	   {
		   s[1]++;
		   count[15]--;count[14]--;count[5]--;
		   }
		   else if(count[19]>0&&count[5]>1&&count[22]>0&&count[14]>0)
		{
			s[7]++;
			count[19]--;count[5]-=2;count[22]--;count[14]--;
		}
		
	   }
	    printf("Case #%d: ",si);
	   for(i=0;i<10;i++)
	   {
		   for(j=0;j<s[i];j++)
		   cout<<i;
	   }
	   cout<<endl;
  }
	 return 0;
}
