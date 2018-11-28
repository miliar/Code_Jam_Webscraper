#include<iostream>
#include<cmath>
#include<cstdio>

using namespace std;
int main()
{
 
 int arr[5][5];
 int brr[5][5];
 int t,i,j,cases;
 cin>>t;
 int first, second, choson;
 int numMatches =0;
 for(cases=1;cases<=t;cases++)
 {
   numMatches =0;                           
   cin>>first;
   for(i=0;i<4;i++)
   { 
     for(j=0;j<4;j++)
     {
        cin>>arr[i][j];
     }
   }
   cin >> second;
   for(i=0;i<4;i++)
    { 
     for(j=0;j<4;j++)
     {
        cin>>brr[i][j];
     }
   }
   for (i = 0 ; i<4 ; ++i)
   {
       for ( j= 0 ;j<4;j++) 
       {
         if(arr[first-1][i] == brr[second -1][j])
         {
           ++numMatches;
           choson = arr[first-1][i];
         }
       }
   }
   if(numMatches == 0)
     cout<<"Case #"<<cases<<": Volunteer cheated!\n";
   else if (numMatches ==1)
     cout<<"Case #"<<cases<<": "<<choson<<"\n";
   else
     cout<<"Case #"<<cases<<": Bad magician!\n";
   
     
}
return 0;
}