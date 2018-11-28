#include<iostream>
#include<fstream.h>
using namespace std;
int main()
{
    int t,n,m,i,j,k,flag=0,l;
    ifstream f1;
    ofstream f2;
    f1.open("bl2.txt",ios::in);
    f2.open("out2.txt");
    f1>>t;
    l=1;
    cout<<t;
    while(l<=t)
    {
    flag=0;
    f1>>n>>m;
    int max1[n],max2[m];
    int a[n][m];
    for(i=0;i<n;++i)
    {
     max1[i]=-1;
     for(j=0;j<m;++j)
     {
      f1>>a[i][j];
      max2[j]=-1;
      }
      }
      for(i=0;i<n;++i)
      {
       for(j=0;j<m;++j)
       {
         if(a[i][j]>max1[i])
         max1[i]=a[i][j];
         }
         }
         for(j=0;j<m;++j)
         {
           for(i=0;i<n;++i)
           {
             if(a[i][j]>max2[j])
             max2[j]=a[i][j];
             }
             }
             for(i=0;i<n;++i)
             {
              for(j=0;j<m;++j)
              {
                if(max2[j]>a[i][j]&&max1[i]>a[i][j])
                {
                 flag=1;
                 f2<<"Case #"<<l<<": "<<"NO"<<endl;
                 break;
                 }
                 }
                 if(flag==1)
                 break;
                 }
                 if(flag==0)
                  f2<<"Case #"<<l<<": "<<"YES"<<endl;
                 l++;
                 }
                  f1.close();
                  f2.close();                
                 return 0;
                 }
