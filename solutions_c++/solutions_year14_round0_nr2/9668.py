#include<iostream>
#include<fstream>
#include<iomanip>


using namespace std;

ifstream ifs("input");

ofstream ofs("output_B");

int main(){
int n;
ifs>>n;
int now=1;
while(now!=n+1){
double C,F,X;
ifs>>C>>F>>X;

double nowF=2.0;
double ans=0.0;
while(X/nowF+ans>X/(nowF+F)+ans+C/nowF){
ans+=C/nowF;
nowF+=F;
}
ans+=X/nowF;
ofs<<"Case #"<<now<<": "<<fixed<<ans<<setprecision(7)<<endl;


now++;
}

}
