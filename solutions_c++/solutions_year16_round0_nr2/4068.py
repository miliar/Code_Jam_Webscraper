#include<iostream>
#include<math.h>
#include<string>
#include<stdio.h>

using namespace std;

int main()
{
  long int t,j,k,i,cou;
  string s;
  cin>>t;
  for(j=0;j<t;j++)
{
   cin>>s;
   k = s.length();
   cou=0;
    if(k==1)
    {
        if(s[0]=='-')
        {
           printf("case #%d: 1\n",j+1);
           continue;
        }
        else
        {
           printf("case #%d: 0\n",j+1);
           continue;
        }
    }
    else
    {
       for(i=0;i<k-1;i++)
            {
             if(s[i]!=s[i+1])
                {
                    cou++;
                }
            }
        if(s[k-1]=='-')
        {
        cou++;
        }
     }
     printf("case #%d: %d\n",j+1,cou);
}
return 0;
}
