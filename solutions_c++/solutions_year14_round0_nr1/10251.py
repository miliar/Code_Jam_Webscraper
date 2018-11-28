#include<iostream>
#include<cstdio>
using namespace std;
long long t,i,j,br,k,pom,x;
long long p[1005],a[1005][1005];
int main()
{
  freopen("A-small-attempt0.in","r",stdin);
  freopen("A-small-attempt0.out","w",stdout);

  cin>>t;

  for(i=1;i<=t;i++)
  {
    br = 0;
    for(j=1;j<=16;j++)
      p[j] = 0;
    cin>>x;
    for(j=1;j<=4;j++)
      for(k=1;k<=4;k++)
        cin>>a[j][k];

    for(j=1;j<=4;j++)
      p[a[x][j]]++;

    cin>>x;
    for(j=1;j<=4;j++)
      for(k=1;k<=4;k++)
        cin>>a[j][k];

    for(j=1;j<=4;j++)
      p[a[x][j]]++;


    for(j=1;j<=16;j++)
      if(p[j] == 2)
      {
        pom = j;
        br++;
      }

    cout<<"Case #"<<i<<": ";

    if(br == 0)
      cout<<"Volunteer cheated!";

    if(br == 1)
      cout<<pom;

    if(br > 1)
      cout<<"Bad magician!";

    cout<<endl;
  }
}
