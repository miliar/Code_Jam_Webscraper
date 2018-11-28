#include<iostream>
#include<cstdlib>
#include<vector>
#include<string>
#include<map>
#include<list>
#include<algorithm>
using namespace std;
#define DEBUG_FLAG 0
#define PRINT(c) (DEBUG_FLAG)?c<<endl:cout<<"";
bool comp(double i, double j)
{
  return i>=j;
}
int main()
{
  int T;
  cin >> T;
  int N;
  vector<double>masnao;
  vector<double>masken;
    
  for(int i=0;i<T;i++)
  {
    cin >> N;
    masnao.assign(N,0.0);
    masken.assign(N,0.0);
    for(int j=0;j<N;++j)
    {
      cin >> masnao[j];
    }
    for(int j=0;j<N;++j)
    {
      cin >> masken[j];
    }      
    sort(masnao.begin(),masnao.end(),comp);
    sort(masken.begin(),masken.end(),comp); 
    int dw=0,max_dw=0;
    
    for(int g=0;g<N;++g)
    {
      
      PRINT(cout<<max_dw)
      dw=0;
      for(int k=0;k+g<N;k++)
      {
        PRINT(cout<<k<<" "<<masnao[k]<<" "<<k+g<<" "<<masken[k+g])
        if(masnao[k] > masken[k+g])
        {
          ++dw;
        }
      }
      (dw>max_dw)?max_dw=dw:dw=dw;
    }
    sort(masnao.begin(),masnao.end());
    sort(masken.begin(),masken.end());
    dw=N;
    for(int m=0;m<N;++m)
    {
      if(masnao[m]<masken[m])
      {
        --dw;
        masken[m]=-1.0;
      }
      else
      {
        for(int o=m+1;o<N;++o)
        {
          if(masnao[m]<masken[o])
          {
            --dw;
            masken[o]=-1.0;
            break;
          }
        }
      }
    } 
    cout<<"Case #"<<i+1<<": "<<max_dw<<" "<<dw<<endl;
    masnao.clear();
    masken.clear();
  }
}
