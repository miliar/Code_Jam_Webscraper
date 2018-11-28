#include <bits/stdc++.h>
using namespace std;
int t,i,l,a,h,n,j,d;
map<int,int>ma;
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
       cinf>>n;
       ma.clear();
       for(i=1;i<=(2*n-1);i++)
       {
           for(j=1;j<=n;j++)
               {
                cinf>>a;
               ma[a]++;
               }
       }
       coutf<<"Case #"<<h<<": ";
       h++;
        map<int,int>::iterator it;
       for(it=ma.begin();it!=ma.end();it++)
       {
           d=it->second;
           if(d%2!=0)
           coutf<<it->first<<" ";
       }
       coutf<<endl;
    }
    return 0;
}

