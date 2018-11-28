#include<bits/stdc++.h>
using namespace std ;
#define ll long long
#define mod 1000000007
int main()
{
    ifstream fin("input.txt") ;
    ofstream fout("output.txt") ;
   int T ;
   fin>>T ;
   for(int t = 1;t<=T;t++)
   {

     int n ; fin>>n ;
     int arr[100] ;
     for(int i = 0;i<n;i++)
     {
         fin>>arr[i] ;
     }
     fout<<"Case #"<<t<<": ";
     bool flag = true  ;
     while(flag == true )
     {
         int ma = 0 ;
         for(int i =0;i<n;i++) if(arr[i]>ma) ma = arr[i] ;
         //fout<<ma<<endl ;
         if(ma==0) flag=false ;
         else{
           int cnt = 0;
           for(int i =0;i<n;i++) if(arr[i]==ma) cnt++ ;
           int k = 0 ;
           for(int i =0;i<n;i++)
           {
               if(arr[i]==ma)
               {
                   arr[i]-- ;
                   char c = 'A'+i ;
                   fout<<c ;
                   k++ ;
                   if((cnt%2==1) || k>1 ) break ;
               }

           }
           fout<<" ";
         }
     }
     fout<<endl ;
   }
}
