#include<iostream>
#include<string>
#include<cmath>
#define unsigned long long int U
using namespace std;
bool palin(int n)
{
     bool flag=0;
     int y=0,x=n;
                while(n>0)
                {
                         y=y*10+n%10;
                         n=n/10; 
                }
                if(y==x)
                return 1;
                else
                return 0;
}
main()
{
      int t;
      cin>>t;
      //string s1,s2;
      int  a,b;
      int casen=0;
      while(t--)
      {
                casen++;
                cin>>a>>b;
                bool fands=0;
                int count=0;
                for(int i=a;i<=b;i++)
                {
                        if(palin(i))
                        {
                                    float y=sqrt(i);
                                    int z=sqrt(i);
                                    if(y==z && palin(z))
                                    {
                                            count++;
                                    }
                        }
                }
      cout<<"Case #"<<casen<<": "<<count<<endl;
      }
//system("pause");
}                                     
                
