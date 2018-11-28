#include<iostream>
using namespace std;

double process(double c, double f, double x, double r, int nf, double t){ double temp_timef=0,temp_timep=0;  temp_timef=t+x/(r+f*(nf+1))+c/(r+f*(nf));
  temp_timep=t+x/(r+f*nf); 
 //cout<<temp_timep<<" "<<temp_timef<<"\n"; 
 if(temp_timep<temp_timef) return temp_timep;  else{      t=t+c/(r+f*nf);      return process(c,f,x,r,nf+1,t);      }
 
}
int main()
{ int t,i=1;
 double c,f,x; cin>>t;
 while(t--) {  cin>>c>>f>>x;  printf("Case #%d: %.7lf\n",i,process(c,f,x,2,0,0));  i++; }}
