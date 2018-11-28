#include<iostream>
using namespace std;
int main()
{
    int t,t1;
    cin>>t;
    t1=t;
    while(t--)
    {
              int a,b,c=0,l[11]={1,4,9,121,484};
              cin>>a>>b;
              for(int i=a;i<=b;i++)
              {
                      for(int j=0;j<11;j++)
                      {
                              if(l[j]==i)
                              {c++;break;}
                      }
              }
              cout<<"Case #"<<t1-t<<": "<<c;
              cout<<endl;
              
    }
    //system("pause");
    return 0;
}
