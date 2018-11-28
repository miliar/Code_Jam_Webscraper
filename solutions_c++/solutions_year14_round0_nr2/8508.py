#include <iostream>
using namespace std;
void minmu(double y, double min,double C,double F,double X,double cnt,int i);
int main() 
{
	int T,i;
	double C,F,X,y,min,cnt=1;
	cin>>T;
	for(i=0;i<T;i++)
  {  cnt=1;
	cin>>C>>F>>X;
    
   y=X/2;
   min=y ;
 minmu(y,min,C,F,X,cnt,i);
    
    	
  }
	return 0;
}
void minmu(double y,double min,double C,double F,double X,double cnt,int i)
{  
	
	y=y+X/(cnt*F+2)-X/((cnt-1)*F+2)+C/((cnt-1)*F+2);
if(y<min)
{
	min=y;
	cnt++;
	minmu(y,min,C,F,X,cnt,i);
}
else
{   std::cout << std::fixed;
	std::cout.precision(7);
	cout<<"Case #"<<i<<": "<<min<<"\n";
}
}
