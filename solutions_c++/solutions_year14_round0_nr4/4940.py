#include<iostream>
#include<algorithm>
using namespace std;
main()
{
      long t,n,i,j,k,x,y,var,z=0;
      double a[1000],a1[1000],b[1000],b1[1000];
      cin>>t;
      while(t--)
      {
                cin>>n;
                for(i=0;i<n;i++){cin>>a[i];b[i]=a[i];}
                 for(i=0;i<n;i++){cin>>a1[i];b1[i]=a1[i];}
                 sort(a,a+n);
                  sort(a1,a1+n);
                  sort(b,b+n);
                  sort(b1,b1+n);
                  y=0;
    /*     for(i=0;i<n;i++)cout<<a[i]<<" ";
                  cout<<endl;
                  for(i=0;i<n;i++)cout<<a1[i]<<" ";
                  cout<<endl;*/
                 for(i=0;i<n;i++)
                 {
                 for(j=0;j<n;j++)
                 {
                 if(a[i]<a1[j])
                 {
                 
                 	a1[j]=0;
                 y++;
                 
                 break;
                 }
                 }
                 }
                 x=0;
               for(k=0;k<n;k++)
               {      for(i=0;i<n-k;i++){a1[i]=b1[n-i-1-k];a[i]=b[i];}
               for(i=n-1;i>n-k-1;i--)a1[i]=0;
               for(i=0;i<k;i++)a[i]=0;
 
 
                         var=0;
                               for(i=0;i<n-k;i++)
                               {
                               for(j=0;j<n-k;j++)
                               {
                               if(a1[i]<a[j])
                               {
                                             a1[i]=0;
                                             a[j]=0;
                                             var++;
                                             break;
                                             }
                                             }}
                                             if(var==n-k)
                                            {x=var; break;}
                                            x=max(x,var);
                                            
                                             }
                                             cout<<"Case #"<<++z<<": "<<x<<" "<<n-y<<endl;
                                             }
                                             return 0;
                                             }
