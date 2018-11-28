#include<iostream>
#include<fstream>

using namespace std;

int main()
{
 ifstream fin("B-small-attempt1.in");
 ofstream fout("ans.txt");
 int n;
 fin>>n;
 int a,b,k,count1;
 int ans;
 for(int i=1;i<=n;i++)
 {
  fin>>a;
  fin>>b;
  fin>>k;
  count1=0;
  for(int j=a-1;j>=0;j--)
  {

    for(int l=b-1;l>=0;l--)
    {
       ans=j&l;
     if(ans>=0 && ans<k)
       {
          count1++;
        //cout<<j<<"&"<<l<<"="<<ans<<endl;
       }

    }
  }
  fout<<"Case #"<<i<<": "<<count1<<endl;
 }

 return 0;
}
