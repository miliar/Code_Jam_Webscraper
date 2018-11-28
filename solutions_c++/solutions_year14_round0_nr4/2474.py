#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int T,N;
double mN[1000+13],mK[1000+13];

int main()
{
  freopen("D.in","r",stdin);
  freopen("D.out","w",stdout);

  scanf("%d",&T);
  for(int cas=1;cas<=T;cas++)
  {
    scanf("%d",&N);
    int ans1(0),ans2(0);
    for(int i=1;i<=N;i++)
      scanf("%lf",&mN[i]);
    for(int i=1;i<=N;i++)
      scanf("%lf",&mK[i]);

    sort(mN+1,mN+1+N);
    sort(mK+1,mK+1+N);

    int iN(1),iK(1);
/*
    for(int i=1;i<=N;i++)
      cout<<mN[i]<<' ';
    cout<<endl;
    
    for(int i=1;i<=N;i++)
      cout<<mK[i]<<' ';
    cout<<endl;
*/
    int Ki(1),Kj(N);
    int Ni(1),Nj(N);
    while(Ni<=Nj)
    {
      if(mN[Ni]>mK[Ki] && Nj>=Ni && Kj>=Ki)
      {
        Ni++;Ki++;
        ans1++;
        continue;
      }
      if(mN[Nj]>mK[Kj] && Nj>=Ni && Kj>=Ki)
      {
        Nj--;Kj--;
        ans1++;
        continue;
      }
      Ni++;Kj--;
    }
    while(iN<=N)
    {
      while(mK[iK]<mN[iN] && iK<=N)
        iK++;
      if(iK==N+1)break;
      if(mK[iK]>mN[iN])
      {
 //       cout<<iK<<' '<<iN<<endl;
        ans2++;
        iN++;
        iK++;
      }
    }
    ans2=N-ans2;
    printf("Case #%d: ",cas);
    printf("%d %d\n",ans1,ans2);
  }
  return 0;
}
