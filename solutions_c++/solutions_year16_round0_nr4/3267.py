#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
        ios_base::sync_with_stdio(0);
       ifstream fin("D-small-attempt0.in",ios::in);
       ofstream fout("3.txt",ios::out);
        int t,count=0;
        fin>>t;
        while(t--)
        {
                int k,c,s;
                fin>>k>>c>>s;
                count++;
                fout<<"Case #"<<count<<": ";
                for(int i=1;i<=k;i++)
                fout<<i<<" ";
                fout<<"\n";
          }
}                
