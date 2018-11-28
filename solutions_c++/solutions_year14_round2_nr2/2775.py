#include <iostream>

using namespace std;

int main()
{  int q,j,i,n,a,b,k,count=0;
   cin>>n;
   for(q=0;q<n;q++)
   { count=0;
     cin>>a;
   cin>>b;
   cin>>k;
   for(i=0;i<a;i++)
   {
      for(j=0;j<b;j++)
   {
       int x=j&i;
       if(x<k)
       count++;
   }
    
   }
   cout<<"Case #"<<q+1<<": "<<count<<endl;
   }
   return 0;
}
