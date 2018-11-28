#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<cstring>
using namespace std;
int cha(char c)
{
   if(c=='1')
      return 1;
    else if(c=='i')
      return 2;
    else if(c=='j')
      return 3;
    else if(c=='k')
      return 4;
}
char cha1(int c)
{
    if(c==1 || c==-1)
      return '1';
    else if(c==2 || c==-2)
      return 'i';
    else if(c==3 || c==-3)
      return 'j';
    else if(c==4 || c==-4)
      return 'k';
}
int main()
{
   freopen("in", "r", stdin);
  freopen("out", "w", stdout);
   int t,l,j,no;
    int r,x,i,p,n;
    int val;
    int a[4][4]={{1,2,3,4},
                 {2,-1,4,-3},
                 {3,-4,-1,2},
                 {4,3,-2,-1}};
    char *s,*s1,c;
    cin>>t;
    p=1;
    while(t--)
    {
        val=1;
        r=0;
        no=0;
    	cin>>l;
        cin>>x;
        s=(char *)malloc(sizeof(char)*l*x+100);
    	s1=(char *)malloc(sizeof(char)*l*x+100);
        cin>>s;
           for(j = 0; j<l; j++) {
		s1[j] = s[j];
	   }
	        s1[l] = '\0';
    	   for(i=1;i<x;i++)
    	   {
                strcat(s,s1);
    	   }
           c=s[0];
           val=cha(c);
           n=1;
           for(i=1;i<strlen(s);i++)
           {
                  if(val==2)
                   {
                       r=i;
                       break;
                   }
                 else
                   {
                       val=n*a[cha(c)-1][cha(s[i])-1];
                       if(val<0)
                        n=-1;
                       else if(val>0)
                        n=1;
                       c=cha1(val); 
                   }
           }
           if(val!=2)
                {
                   no=1;goto end;
                }
           c=s[r];
           val=cha(c);
           n=1;
           for(i=r+1;i<strlen(s);i++)
           {
                 if(val==3)
                   {
                       r=i;
                       break;
                   }
                 else
                   {
                       val=n*a[cha(c)-1][cha(s[i])-1];
                       if(val<0)
                       n=-1;
                        else if(val>0)
                       n=1;
                       c=cha1(val);
                   }
           }
           if(val!=3)
                {
                   no=1;goto end;
                }
               c=s[r];
               val=cha(c);
               n=1;
          for(i=r+1;i<strlen(s);i++)
           {
                       val=n*a[cha(c)-1][cha(s[i])-1];
                       if(val<0)
                       n=-1;
                       else if(val>0)
                        n=1;
                       c=cha1(val);
           }
           if(val!=4)
                {
                   no=1;
                   goto end;
                }
            end:
           if(no==0)
    	   cout<<"Case #"<<p<<": YES"<<endl;
           else if(no==1)
    	   cout<<"Case #"<<p<<": NO"<<endl;
           p++;
    	   free(s);
           free(s1);
    }
	return 0;
}
