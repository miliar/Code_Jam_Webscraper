#include<bits/stdc++.h>
using namespace std;
int main()
{
  ios_base::sync_with_stdio(false);
  int t=1,cases;
  ifstream fin;
  fin.open("inp1.in");
  ofstream fout;
  fout.open("out1.txt");
  fin>>cases;
  while(cases--)
  {
      int n;
      fin>>n;
      string s;
      fin>>s;
      int sum=s[0]-'0',ans=0;
      for(int i=1;i<=n;i++)
       {
           //fout<<ans<<endl;
           if(sum<i && ((s[i]-'0')!=0) )
            {ans+=i-sum;
    //cout<<i<<endl;
        sum+=(s[i]-'0')+ans;}
        else
            sum+=(s[i]-'0');
       // cout<<sum<<endl;
       }
   fout<<"Case #"<<t<<": "<<ans<<endl;
   t++;
  }
}
