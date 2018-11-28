#include<bits/stdc++.h>
using namespace std;

void solve(int hula)
{
      int l;
      int count=0,temp;
      int total=0;
      char c;
      int i=0;
      scanf("%d",&l);
      c=getchar_unlocked();
      while(c<'0' || c>'9'){c=getchar_unlocked();}
      while(c>='0' && c<='9')
      {
            if(i==0)
                  total+=c-'0';
            else if(total>=i)
                  total+=c-'0';
            else
            {     
                  temp=i-total;
                  count+=temp;
                  total+=temp;
                  total+=c-'0';
            }
            c=getchar_unlocked();
            i++;
      }
      printf("Case #%d: %d\n",hula,count);
}
int main()
{
      int t;
      scanf("%d",&t);
      int i=1;
      while(t--)
      {
            solve(i);
            i++;
      }
      return 0;
}
