#include <iostream>
#include <iomanip>

using namespace std;
double c;
double f;
double x;
double mintime=0;
int main()
{
int ciclo=0;

   cin>>ciclo;
   for(int i=1;i<=ciclo;i++){
       cin>>c;
       cin>>f;
       cin>>x;
       mintime=x/2;
       double time=0;
       time=c/(2);
       if(mintime>time+(x/(2+(f)))){
           //cout<<time<<"\t";
           //cout<<time+(x/(2+(f)))<<" "<<endl;
           mintime=time+(x/(2+(f)));
       }
       for(int j=1;j<100000;j++){
           time=time+(c/(2+(f*j)));
           //cout<<j<<"\t";
           //cout<<(c/(2+(f*j)))<<"\t";;
           //cout<<time<<"\t" ;
           //cout<<time+(x/(2+(f*(j+1))))<<" "<<endl;
           if(time+(x/(2+(f*(j+1))))<mintime){
               mintime=time+(x/(2+(f*(j+1))));
           }else{
               break;
           }
           
       }
       std::cout << std::fixed;
       std::cout << std::setprecision(7);
       cout<<"Case #"<<i<<": "<<mintime<<endl;
   }
   
   return 0;
}
