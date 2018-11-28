#include <bits/stdc++.h>
#define llu unsigned long long

using namespace std;

int main () {
  int T,t1,t2;
  cin>>T;


  for(int iter=1;iter<=T;iter++)
  {
	  llu first[4],second[4],temp;
  std::vector<llu> v(8);
  std::vector<llu>::iterator it;
      cin>>t1;
      for(int i=0;i<4;i++)
      {
          for(int j=0;j<4;j++)
          {
              if(i==t1-1)
              {
                cin>>first[j];
              }
              else
              {
                cin>>temp;
              }
          }
      }
      cin>>t2;
      for(int i=0;i<4;i++)
      {
          for(int j=0;j<4;j++)
          {
              if(i==t2-1)
              {
                cin>>second[j];
              }
              else
              {
                cin>>temp;
              }
          }
      }
      std::sort (first,first+4);
      std::sort (second,second+4);

      it=std::set_intersection (first, first+4, second, second+4, v.begin());
      v.resize(it-v.begin());

      cout<<"Case #"<<iter<<": ";
      if(v.size()==0)   cout <<"Volunteer cheated!"<<endl;
      else if(v.size()==1)  cout <<*(v.begin())<<endl;
      else cout <<"Bad magician!"<<endl;

  }

  return 0;
}
