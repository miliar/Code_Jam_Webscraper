#include<iostream>
 using namespace std;

 int main()
 {
     int t,f,l,count,p,i,j,m;
     int arr[4][4];
     int brr[4][4];
     int crr[4];

     cin>>t;
     m=1;
     while(t--)
     {
         count=0;
         cin>>f;

         for(i=0;i<4;i++)
         {
             for(j=0;j<4;j++)
             {
                 cin>>arr[i][j];
             }
         }

         cin>>l;

         for(i=0;i<4;i++)
         {
             for(j=0;j<4;j++)
             {
                 cin>>brr[i][j];
             }
         }

         for(i=0;i<4;i++)
         {
             for(j=0;j<4;j++)
             {
                 if(arr[f-1][i] == brr[l-1][j])
                 {

                     crr[count]=arr[f-1][i];
                     count++;

                 }
             }
         }

         if(count==1)
         {
             cout<<"Case #"<<m<<":"<<" "<<crr[0]<<endl;
             m++;
         }
         if(count>=2)
         {
             cout<<"Case #"<<m<<": Bad magician!"<<endl;
             m++;
         }
         if(count==0)
         {
             cout<<"Case #"<<m<<": Volunteer cheated!"<<endl;
             m++;
         }

     }
     return 0;
 }
