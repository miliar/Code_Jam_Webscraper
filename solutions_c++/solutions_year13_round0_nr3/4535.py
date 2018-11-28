# include<iostream>
# include<cstdio>
# include<cmath>
# include<fstream>
# include<sstream>
# include<vector>
# define N 10001
# define M 1000000
using namespace std;
int chck(int a)
{
                    int j,n,d=1,f=10;
                     j=a;
                     n=1;
                     while(j)
                     {
                             n*=10;
                             j/=10;
                     }
                     n/=10;
                     j=a;
                     while(j)
                     {
                             if(j/n==j%f)
                             {
                                         j%=n;
                                         j/=f;
                                         n/=100;
                             }
                             else
                             {
                                 d=0;
                                 break;
                             }
                     }
                     return d;
}
int main()
{
    int t,a,b,i,c,j,x=0,css=0;
    int arr[N]={0};
    for(i=1;i<=M;++i)
    {
                     j=sqrt(i);
                     if(j*j==i)
                     {
                               // cout<<i<< " ";
                               if(chck(i)&&chck(j))
                               arr[x++]=i;
                     }
    }     
    //cout<<chck(121);
    --x;               
    //for(i=0;i<x;++i)cout<<arr[i]<<" ";       
    freopen("C-small-attempt0.in","r",stdin);
    cin>>t;
    cin.ignore();
    ofstream m;
    m.open("o1.txt");
    while(t--)
    {
              c=0;
              cin>>a>>b;
              for(i=0;i<x;++i)
              {
                              if(arr[i]>=a && arr[i]<=b)
                              ++c;
                              if(arr[i]>b)
                              break;
              }
              m<<"Case #"<<++css<<": "<<c<<endl;
              cin.ignore();
    }
    m.close();
    return 0;
}
