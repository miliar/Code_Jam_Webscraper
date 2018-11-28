#include <iostream>
#include <stdio.h>
#include <fstream>
#include <math.h>
using namespace std;
int fair(int f){
    int o,a,b,c,d,p;//,e,g,h,j,m,n,q,w,r,t;
    //cout<<f<<endl;
a = ((f % 10) / 1);
//cout<<a<<endl;
a=a*1000;
b = ((f % 100) / 10);
b=b*100;
c = ((f % 1000) / 100);
c=c*10;
d = ((f % 10000) / 1000);
d=d*1;
/*e = ((f % 100000) / 10000);
e=e*1000000000;
g = ((f % 1000000) / 100000);
g=g*100000000;
h = ((f % 10000000) / 1000000);
h=h*10000000;
j = ((f % 100000000) / 10000000);
j=j*1000000;
m = ((f % 1000000000) / 100000000);
m=m*100000;
n = ((f % 10000000000) / 1000000000);
n=n*10000;
q = ((f % 100000000000) / 10000000000);
q=q*1000;
w = ((f % 1000000000000) / 100000000000);
w=w*100;
r = ((f % 10000000000000) / 1000000000000);
r=r*10;
t = ((f % 100000000000000) / 10000000000000);
t=t*1;*/
//cout<<a<<endl<<b<<endl<<c<<endl<<d<<endl;
p = a+b+c+d;//+e+g+h+j+m+n+q+w+r+t;
//cout<<p<<endl;
for(o=0;o<15;o++){if(p%10==0){p=p/10;}}
//cout<<p<<endl;
if(p==f){return true;};


return false;
}

int main()
{      ofstream myfile;
       myfile.open ("output.txt");
       ifstream his;
       his.open ("C-small-attempt0.in");
    int T;
his>>T;
int x,y;
int i,v,z=0;
 for(i=1;i<=T;i++){
        his>>x>>y;
      for(int f=x;f<=y;f++){
        v=pow(f,0.5);
      if(fair(f)){if(pow(f,0.5)==v){if(fair(f)){z++;}}
}}
myfile<<"Case #"<<i<<": "<<z<<endl;
z=0;
 }
return 0;
}
