#include<bits/stdc++.h>
using namespace std;
long int t,n,h,i,g;
map<long int,long int> m;
int main()
{
  ifstream cinf;
  ofstream coutf;
  cinf.open("input.txt");
  coutf.open("ans.txt");
  cinf>>t;
  h=1;
  while(t--)
  {
      m.clear();
      cinf>>n;
      i=1;
      while(m.size()<10&&n!=0)
      {
          g=i*n;
          i++;
          while(g>0)
          {
              m[g%10]=1;
              g=g/10;
          }
      }
      if(n!=0)
      coutf<<"Case #"<<h<<": "<<(i-1)*n<<endl;
      else
      coutf<<"Case #"<<h<<": INSOMNIA"<<endl;
      h++;
  }
    return 0;
}
