#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int a[1000][1000];
vector <int> vc;
void run()
{  int t,cnt=1;
freopen("A-small-attempt.in","r",stdin);
freopen("A-small-attempt.out","w",stdout);
  scanf("%d",&t);
  while(t--)
  {
      int c1;
      vc.clear();
      scanf("%d",&c1);
      for(int i=0;i<4;i++)
        for(int j=0;j<4;j++){
        int a;
        scanf("%d",&a);
            if(i==c1-1) vc.push_back(a);
        }
      scanf("%d",&c1);
      for(int i=0;i<4;i++)
        for(int j=0;j<4;j++){
        int a;
        scanf("%d",&a);
            if(i==c1-1) vc.push_back(a);
        }
        sort(vc.begin(),vc.end());
  int flag=0;
  int ans;
  for(int i=1;i<vc.size();i++){
    if(vc[i]==vc[i-1]) {flag++;
    ans=vc[i];
    }
  }
  printf("Case #%d:",cnt++);
  if(!flag) printf(" Volunteer cheated!\n");
  else if(flag==1) printf(" %d\n",ans);
  else printf(" Bad magician!\n");



  }





}
int main()
{

   run();
    return 0;
}
