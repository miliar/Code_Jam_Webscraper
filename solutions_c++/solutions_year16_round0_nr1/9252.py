#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
    int t;
    ifstream fin("A-large.in");
	ofstream fout("output.txt");
    fin>>t;
    for(int w=1;w<=t;w++)
    {
        long long n,m,flag=0,count=0,l;
        fin>>n;
        int a[10]={0};
        m=n;
        if(n==0)
            fout<<"Case #"<<w<<": "<<"INSOMNIA"<<endl;
        else
        {
        for(int i=1;i<100000000;i++)
        {
            m=n*i;
            while(m)
            {
                int k=m%10;
                a[k]=1;
                m/=10;
            }
            if(flag==0)
            {
                for(int j=0;j<=9;j++)
                {
                    if(a[j]==1)
                    {
                        count++;
                    }
                }
            }
          if(count==10)
          {
              l=n*i;
              break;
          }
          else{count=0;}
        }
        fout<<"Case #"<<w<<": "<<l<<endl;
      }
    }
return 0;
}
