#include <bits/stdtr1c++.h>
using namespace std;



int main()

{//   char index;
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

   int index=-1,index2=-1;
   int t,n,p;
   int a[26];
   char senate1,senate2;
   cin>>t;
    int max=0;


   for(int i=1;i<=t;i++)
   {
       cin>>n;
       for( int j=0;j<n;j++)
         {   cin>> p;
             a[j]=p;
         }

     cout<<"Case #"<<i<<":"<<" " ;
      while(*min_element(a,a+n)>0)
//     for(int h=0;h<10;h++)
       {
//              cout<<"checking loop"<<*min_element(a,a+n)<<endl;
           for(int j=0;j<n;j++){ if (a[j]>max) {max=a[j];index=j;}}
           for(int j=0;j<n;j++){ if (a[j]==max and j!=index) index2=j;}

            if (max==1 )
            {
                 //senate1=index+65;cout<<senate1<<" ";a[index]--;index=-1;
               int g;
                  for( g=0;g<n-2;g++)
                    {  senate1=g+65;
                       cout<<senate1<<" ";
                    }
                    senate1=g+65;senate2=g+66;
                    cout<<senate1<<senate2<<" ";

            index=index2=-1;
                 break;

            }

              max=0;

           if (index>-1 && index2>-1)
             {  senate1=65+index;senate2=65+index2;
                 cout<<senate1<<senate2<<" ";
                 a[index]--;a[index2]--;
                 index=index2=-1;
             }
            else if (index>-1)
                 {
                     senate1=index+65;cout<<senate1<<" ";a[index]--;index=-1;
                 }
            else if (index2>-1)
                 {
                     senate2=index2+65;cout<<senate2<<" ";a[index2]--;index2=-1;
                 }


           }
          cout<<endl;
       }


return 0;

}
