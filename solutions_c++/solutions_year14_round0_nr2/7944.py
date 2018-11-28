#include <fstream>
#include <iostream>
#include<iomanip>
using namespace std;
int main()
{
  long double c,x,f,prod=2,ans1,ans2,temp;
  int test,i=0;
  ifstream fin;
  ofstream fout;
  fin.open("B-large.in");
  fout.open("B-largeo.in");
  fin>>test;
  while(test>0)
  {
    fin>>c;
    fin>>f;
    fin>>x;
    prod=2;
    ans1=x/2;
    ans2=0;
    while(1)
    {
      ans2+=c/prod;
      prod+=f;
      ans2+=x/prod;
      if(ans2<ans1)
      {
        ans1=ans2;
        ans2-=x/prod;
      }
      else
        break;

    }
    fout<<"Case #"<<i+1<<": "<<std::fixed<<std::setprecision(7)<<ans1<<endl;
    test--;
    i++;
  }
  return(1);
}
