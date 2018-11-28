#include<iostream>
#include<math.h>
#include<algorithm>
using namespace std;
int main()
{
      freopen("C-small-attempt0.in","r",stdin);
      freopen("csmall.txt","w",stdout);
      int a[10005]={0},i;
      a[1]=1;
      a[4]=1;
      a[9]=1;
      a[121]=1;
      a[484]=1;
      /*
      for(i=121;i<1001;i++)
      {
                           int x=0;
                           int z=i;
                           while(z!=0)
                           {
                                      x=10*x+z%10;
                                      z=z/10;
                           }
                           if(x==i)
                           a[i]=1;
      }
        */                   
      int t;
      cin>>t;
      int c=1;
      while(t--)
      {
                int a1,b;
                cin>>a1>>b;
                int count=0;
                for(i=a1;i<=b;i++)
                {
                                 if(a[i]==1)
                                 {
                                            //int x=pow(a[i],0.5);
                                            //if((a[x]==1)&&(x*x==i))
                                            count++;
                                 }
                }
                cout<<"Case #"<<c<<": ";
                c++;
                cout<<count<<endl;
      }
      return 0;
}
