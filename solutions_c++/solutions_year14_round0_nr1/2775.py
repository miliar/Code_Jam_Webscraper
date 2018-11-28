#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
int arr[6][6];
vector<int> a,b;
int main()
{
    freopen("qns.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    int t,row,ans;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
      a.clear();
      b.clear();
      scanf("%d",&row);
      row--;
      for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
          scanf("%d",&arr[i][j]);
      for(int j=0;j<4;j++)
          a.push_back(arr[row][j]);
      sort(a.begin(),a.end());
      scanf("%d",&row);
      row--;
      for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
          scanf("%d",&arr[i][j]);
      for(int j=0;j<4;j++)
          b.push_back(arr[row][j]);
      sort(b.begin(),b.end());
      int cnt=0;
      for(int i=0;i<a.size();i++)
        for(int j=0;j<b.size();j++)
          if(a[i]==b[j])
          {
            cnt++;
            ans=a[i];
          }
      if(cnt==0)
        printf("Case #%d: Volunteer cheated!\n",test);
     else if(cnt==1)
        printf("Case #%d: %d\n",test,ans);
     else
        printf("Case #%d: Bad magician!\n",test);
    }
    return 0;
}
