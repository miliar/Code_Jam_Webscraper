#include<iostream>
#include<fstream>
#include<iomanip>
double t=2.0000000,ti=0;
using namespace std;
void time(double c,double f,double x){
double m,n,o;
m=c/t;
n=m+(x/(t+f));
o=x/t;
if(o<n)ti=ti+o;
else{ti=ti+m;
t=t+f;
time(c,f,x); 
}
}
int main(){
ifstream fin;
ofstream fout;
int s;
double c,f,x,a=2.0,tt=0.0;
fin.open("B-large.in");
fin>>s;
for(int i=1;i<=s;i++){tt=0.0;
fin>>c>>f>>x;
time(c,f,x);
tt=tt+ti;
fout.open("testo2.txt",std::ios_base::app);
fout<<"Case #"<<i<<": ";
fout<<std::fixed<<setprecision(7)<<tt<<endl;
fout.close();
t=2.000000;ti=0.000000;
}
fin.close();
return 0;
}
