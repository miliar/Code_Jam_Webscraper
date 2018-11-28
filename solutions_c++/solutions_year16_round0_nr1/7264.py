#include<iostream>
using namespace std ;
int arr[10] ;
int main()
{
   long n , i ,z=1,no ;
      int m =1 ;
   cin>>n ;
   while(z<=n)
   {
       cin>>i;
       if(i==0)
       {
           cout<<"Case #"<<z<<": INSOMNIA"<<endl;
       }
       else
       {  m=1 ;
          label :
          no=i*m ;
          while(no>0)
          {
              arr[no%10]=1;
              no=no/10;
          }
          for(int x=0;x<=9;x++)
          {
              if(arr[x]==0)
              {
                  m++;
                  goto label ;

              }

          }
          cout<<"Case #"<<z<<": "<<i*m<<endl;



          }

            for(int x=0;x<=9;x++)
          {
              arr[x]=0;

          }




         z++;
       }








    return 0 ;
}
