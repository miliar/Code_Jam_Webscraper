#include <iostream>
#include <vector>
#include <map>
#include <cstring>
#include <list>
#include <queue>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <stack>
#include <sstream>
#include <bitset>
#include <set>



using namespace std;



int main()
{

    freopen("a.txt","r",stdin);
   freopen("b.txt","w",stdout);
  int T,n,cased=0;
    string a,b;
  cin>>T;

  while(T--)
  {
      cin>>n;
      cin>>a>>b;
      int ans=0;
      bool flag=true;
      int i=0,j=0,starti=0,startj=0;
      while(1)
      {

          starti=i,startj=j;


         // cout<<i<<" iii "<<j<< " jjjj "<<endl;
          if(a[i]!=b[j]){flag=false;break;}
          if(i>=a.size() or j>=b.size())break;
          while(a[i]==a[i+1] && i+1<a.size())i++;//cout<<"i "<<i<<endl;}
          while(b[j]==b[j+1] && j+1<b.size())j++;//cout<<"j "<<j<<endl;}
          ans+=abs((i-starti)-(j-startj));
          // cout<<starti<<" "<<i<<" "<<startj<<" "<<j<<endl;
          i++;j++;

      }
      if(flag)
      printf("Case #%d: %d\n",++cased,ans);
      else printf("Case #%d: Fegla Won\n",++cased);
  }



return 0;
}


