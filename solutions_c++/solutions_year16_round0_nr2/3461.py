#include<bits/stdc++.h>
using namespace std;

void flip(int a[],int x)
 {
     int i,temp;
     for(i=0;i<x/2;i++)
     {
        temp=a[i];
        a[i]=a[x-i]*-1;
        a[x-i]=a[i]*-1;

     }
     if(x%2==0)
        a[i]*=-1;


 }

 int main()
  {
    freopen("B-large.in","r",stdin);
     freopen("output.txt","w",stdout);

    int t;
    scanf("%d",&t);


    int i;
    for(i=1;i<=t;i++)
     {
          string s;
          cin>>s;
          int j,k;
          int arr[s.size()];
          for(j=0;j<s.size();j++)
           {
                if(s[j]=='+')
                  arr[j]=1;
                else
                arr[j]=-1;
           }
           int ctr=0;
          for(j=0;j<s.size()-1;j++)
           {
                 if(arr[j]!=arr[j+1])
                     {
                       flip(arr,j);
                       ctr++;

                       }
           }
           if(arr[j]==-1)
             ctr++;

             printf("Case #%d: %d\n",i,ctr);

     }


  }
