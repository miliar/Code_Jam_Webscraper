#include<iostream>
#include<fstream>
using namespace std;

int main ()
{
    freopen("input_A.txt","r",stdin);
    freopen("output_A.txt","w",stdout);
    int t;
    cin>>t;
    for(int o=1;o<=t;o++)
    {
      int n;

      scanf("%1d ",&n);



    int a[n+2];

      for(int i=0;i<=n;i++)
      {
          scanf("%1d ",&a[i]);
      }


        if(n==0)
        {
            cout<<"Case #"<<o<<": "<<0<<endl;
            continue;
        }
    int count=a[0];
      int need=0,res=0,p;
      for(int i=1;i<=n;i++)
      {


          if(i>count){ need++; count++; }
        count += a[i];


      }

      cout<<"Case #"<<o<<": "<<need<<endl;
      }
    }


