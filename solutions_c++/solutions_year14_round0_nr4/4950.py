#include<iostream>
#include<algorithm>
using namespace std;
main()
{
      long t,n,i,j,k,x,y,variable,z=0;
      double arr[1000],arr1[1000],brr[1000],brr1[1000];
      cin>>t;
      while(t--)
      {
                cin>>n;
                for(i=0;i<n;i++){cin>>arr[i];brr[i]=arr[i];}
                 for(i=0;i<n;i++){cin>>arr1[i];brr1[i]=arr1[i];}
                 sort(arr,arr+n);
                  sort(arr1,arr1+n);
                  sort(brr,brr+n);
                  sort(brr1,brr1+n);
                  y=0;
                 for(i=0;i<n;i++)
                 {
                 for(j=0;j<n;j++)
                 {
                 if(arr[i]<arr1[j])
                 {

                 	arr1[j]=0;
                 y++;

                 break;
                 }
                 }
                 }
                 x=0;
               for(k=0;k<n;k++)
               {      for(i=0;i<n-k;i++){arr1[i]=brr1[n-i-1-k];arr[i]=brr[i];}
               for(i=n-1;i>n-k-1;i--)arr1[i]=0;
               for(i=0;i<k;i++)arr[i]=0;


                         variable=0;
                               for(i=0;i<n-k;i++)
                               {
                               for(j=0;j<n-k;j++)
                               {
                               if(arr1[i]<arr[j])
                               {
                                             arr1[i]=0;
                                             arr[j]=0;
                                             variable++;
                                             break;
                                             }
                                             }}
                                             if(variable==n-k)
                                            {x=variable; break;}
                                            x=max(x,variable);

                                             }
                                             cout<<"Case #"<<++z<<": "<<x<<" "<<n-y<<endl;
                                             }
                                             return 0;
                                             }
