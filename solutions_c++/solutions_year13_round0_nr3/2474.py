#include<iostream>
#include<fstream>
#include<math.h>
#include<vector>
bool fun(long long a)
{
     int ch[20],s=0;
     while(a)
     {
             ch[s++]=a%10;
             a=a/10;
     }
     for(int i=0;i<s/2;i++)
             if(ch[i]!=ch[s-i-1])
                                 return false;
     return true;
}
using namespace std;
int main()
{
    vector<long long> v;
    for(long long i=1;i<=3000000;i++)
    {
            if(fun(i) && fun(i*i))
            {
                  v.push_back(i); 
                  //cout<<i<<endl;   
            }
    }
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");
    int t,l=0;
    fin>>t;
    while(t--)
    {
              l++;
              long long p,q,c=0;
              fin>>p>>q;
              for(int i=0;i<v.size();i++)
              {
                      if(v[i]*v[i]>=p && v[i]*v[i]<=q)
                                 c++;
              }
              fout<<"Case #"<<l<<": "<<c<<"\n";
    }
    //system("pause");
    return 0;
}
