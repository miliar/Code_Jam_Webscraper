#include<iostream>
#include <fstream>
#include<iomanip>
using namespace std;
double c,f,x;
int t;
int main(){
ofstream ocout;
ocout.open("test3.txt");
scanf("%d",&t);
int i,j,k;
double time1,time2;
double sudu,result;
for(k=1;k<=t;k++){
scanf("%lf%lf%lf",&c,&f,&x);
sudu=2.0;
result=0;
while(true){
time1=x/sudu;
time2=c/sudu+x/(sudu+f);
if(time1<=time2)
{
result+=time1;
break;
}
else
  {
  result+=c/sudu;
  sudu+=f;
  }
}
//Case #4: 526.1904762
ocout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<result<<endl;

//printf("Case #%d: %.7lf\n",k,result);                  
}
ocout.close();
//system("pause");
return 0;
}
