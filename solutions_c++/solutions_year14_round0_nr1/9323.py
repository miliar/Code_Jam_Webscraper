#include <bits/stdc++.h>

using namespace std;

int mapfirst[4][4];
int mapsecond[4][4];

int main()
{
  int t;
  cin>>t;
  for(int k=1;k<=t;++k){
    int first,second;
    cin>>first;
    for(int i=0;i<4;++i)
      for(int j=0;j<4;++j)
        cin>>mapfirst[i][j];
    cin>>second;
    for(int i=0;i<4;++i)
      for(int j=0;j<4;++j)
        cin>>mapsecond[i][j];
    int count=0,res=0;
    for(int i=0;i<4;++i)
      for(int j=0;j<4;++j)
        if(mapfirst[first-1][i]==mapsecond[second-1][j]){
          count++;
          res=mapfirst[first-1][i];
        }
    switch(count){
    case 0:
      cout<<"Case #"<<k<<": Volunteer cheated!\n";
      break;
    case 1:
      cout<<"Case #"<<k<<": "<<res<<"\n";
      break;
    default:
      cout<<"Case #"<<k<<": Bad magician!\n";
    }
  }
  return 0;
}
