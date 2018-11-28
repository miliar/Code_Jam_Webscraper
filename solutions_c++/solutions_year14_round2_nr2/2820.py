#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include<set>
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
using namespace std;
int main()
{




 ofstream fout("ans.out");
 ifstream fin ("B-small-attempt0.in");

 int t;fin>>t;
 int f=0;
 while (t--){

 int a,b,k;fin>>a>>b>>k;

long int ctr=0;
  for (int i=0;i<min(a,b);i++){
      for (int j=0;j<max(a,b);j++){

      int c =i&j;
      if (c<k)
       ++ctr;

      }
 }

 ++f;
 fout<<"Case #"<<f<<":"<<" "<<ctr<<"\n";


 }



  return 0;
}
