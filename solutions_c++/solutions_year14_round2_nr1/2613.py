#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

int main()
{
 int t,j,k;
 cin>>t;
 for(int i=0;i<t;i++)
 {
  char s1[101],s2[101];
  int n;
  cin>>n;
  cin>>s1>>s2;
  int counter=0;
  for(j=0,k=0;s1[j]!='\0' && s2[k]!='\0'; )
  {
	if(s1[j]!=s2[k])
	   break;
	else
	{
	  if((s1[j+1]==s2[k+1]) || ((s1[j]!=s1[j+1]) && (s2[k]!=s2[k+1])))
		j++,k++;
	  else
	    {
		 if(s1[j]==s1[j+1])
	       j++;
	     if(s2[k]==s2[k+1])
	        k++;
	    counter++;
		}
	}
   }
   if(s1[j]=='\0' && s2[k]=='\0')
     cout<<"Case #"<<i+1<<": "<<counter<<endl;
   else
     cout<<"Case #"<<i+1<<": Fegla won"<<endl;
}
return 0;
}
