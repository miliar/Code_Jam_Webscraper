#include <iostream>

using namespace std;
int nt;
double c[100];
double x[100];
double f[100];
int mul=2;
int main()
{
    cin>>nt;
 for(int i=0;i<nt;i++)
 {
 cin>>c[i];
 cin>>f[i];
 cin>>x[i];
 }
 // case 1
 for(int i=0;i<nt;i++)
 {
     mul=2;
 double c1=x[i]/2;
 double c3=c[i]/2+c[i]/(2+f[i]);
 double c2=c[i]/2+x[i]/(2+f[i]);  
 
  while(c2<c1)
 {
     c1=c2;
   c2=c3+x[i]/(2+mul*f[i]); 
   c3=c3+c[i]/(2+mul*f[i]);
    mul++;
 
    
 }

std::cout.precision(10);
std::cout.setf( std::ios::fixed, std:: ios::floatfield );
cout<<"Case #"<<i+1<<": ";
std::cout<<c1<<endl;

 }
   return 0;
}
