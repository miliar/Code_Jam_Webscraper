#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;
int main()
{
    int t,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
      int n,j,i,c=0,ct=0,l;
      cin>>n;
      double a[n],b[n],temp;
      for(i=0;i<n;i++)
            cin>>a[i];
      for(j=0;j<n;j++)
        cin>>b[j];
      for(i=0;i<n-1;i++)
        for(j=0;j<n-1-i;j++)
        if(fabs(a[j]-a[j+1])>0.000001)
      {
          temp=a[j];
          a[j]=a[j+1];
          a[j+1]=temp;
      }
       for(i=0;i<n-1;i++)
        for(j=0;j<n-1-i;j++)
        if((b[j]-b[j+1])>0.000001)
      {
          temp=b[j];
          b[j]=b[j+1];
          b[j+1]=temp;
      }
      i=0;
      j=0;
      while(i<n && j<n)
      {
          for(l=i;l<n;l++)
            if((a[l]-b[j])>0.000001)
            break;
            cout<<"l ";
            i=l;
            if(i<n)
                j++;
      i++;
      }
      c=j;
      for(i=0;i<n;i++)
        if((a[i]-b[i])>0.000001)
        ct++;
    cout<<"Case #"<<k<<": ";
    cout<<c<<" "<<ct<<endl;
    }
    return 0;
}
