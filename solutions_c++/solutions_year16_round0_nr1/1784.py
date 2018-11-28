#include <iostream>
#include <bits/stdc++.h>
using namespace std;
unordered_map <int,int> hold;
int checkdigit(unsigned long long n)
{  int tmp=1;
   while(n!=0)
   {
      tmp = n%10;
      hold[tmp]++;
      n = n/10;
   }
   if(hold.size()==10) return 1;
   else return 0;
}
int main()
{
  ios_base::sync_with_stdio(false);
  //freopen("input1.txt","r",stdin);
  //freopen("output1l.txt","w",stdout);
  int t; cin >> t;
  for(int k = 1;k<=t;k++)
  {   int i=1;
	  hold.clear();
     unsigned long long n,tmp; cin >> n;
     if(n==0){ printf("Case #%d: INSOMNIA\n",k); continue;}
     while(1)
     {
       tmp = i*n;
       i++;
       if(checkdigit(tmp)) break;
     }
     printf("Case #%d: %llu\n",k,tmp);
     
  }
return 0;
}

