#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
int a[100][100];
int l0,l1,l2,l3;
int h,w,t;
bool g,f1,f2;
int main()
{
  freopen("blarge.in","r",stdin);
  freopen("lawn2.out","w",stdout);
  cin>>t;
  for(l0=1;l0<=t;l0++)
  {
    cin>>h>>w;
    for(l1=1;l1<=h;l1++)
      for(l2=1;l2<=w;l2++)
        cin>>a[l1][l2];
    g=true;
    for(l1=1;l1<=h;l1++)
        for(l2=1;l2<=w;l2++)
        {
          f1=true;
          f2=true;
          for(l3=1;l3<=h;l3++)
            if(a[l3][l2]>a[l1][l2])
              f1=false;
          for(l3=1;l3<=w;l3++)
            if(a[l1][l3]>a[l1][l2])
              f2=false;
          if(f1==false&&f2==false)
          {
            //cout<<l1<<" "<<l2<<endl;
            g=false;
          }
        }
    cout<<"Case #"<<l0<<": "<<(g?"YES":"NO")<<endl;
  }
  fclose(stdin);
  fclose(stdout);
  return 0;
}
