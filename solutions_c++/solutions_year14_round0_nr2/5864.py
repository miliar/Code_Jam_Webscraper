#include <iostream>
#include <math.h>
#include <cstdio>
using namespace std;

int main()
{
   int t;
   double c,f,x;
   int c1=1;
   double mx,aux,mxs,cf,ax;
   cin>>t;
   while(t--){
       cin>>c>>f>>x;
       mx=x/2;
       aux=0;
       ax=0;
       cf=2;
       while(true){
           aux=(c/cf)+ax;
           ax=aux;
           //cout<<aux<<"aaaaaaaaaa";
           cf+=f;
           aux+=(x/cf);
           //cout<<aux<<endl;
           if(aux>mx)break;
           mx=aux;
           
       }
       cout<<"Case #"<<c1++<<": ";
       printf("%.7f",mx);
       cout<<endl;
       
   }
   return 0;
}

