#include <fstream>
#include <cstdlib>
#include <iostream>
using namespace std;
int main() {
int t;
double c;
double f;
double x;


  ifstream myReadFile;

    myReadFile.open("file.text");
  ofstream out;
    out.open("sluo.text");

  myReadFile>>t;
  std::cout.precision(7);
  std::cout.setf( std::ios::fixed, std:: ios::floatfield ); 
for(int i=0;i<t;i++)
{  myReadFile>>c;
   myReadFile>>f;
   myReadFile>>x;
   double sum=0,sum1=0,sum2=0;
   if(x<c)
    cout<<"Case #"<<i+1<<": "<<x/2<<endl;
   else{
       
       int j=0;
        int z=1;
       while(z==1){
       if(j!=0)
       sum=sum+c/(2+((j-1)*f));
       sum1=sum+x/(2+j*f);
       sum2=sum+c/(2+j*f)+(x/(2+(j+1)*f));
    
       
       j++;
       if(sum1<sum2)
         z=0;
       

          }
        cout<<"Case #"<<i+1<<": "<<sum1<<endl;


}
   

}

}
