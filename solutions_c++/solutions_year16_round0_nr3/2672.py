#include <bitset>
#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;
typedef unsigned long long ll;

#define aggr

bool dv(ll m ,ll &n){ll a=(m/2); ll x=m; //cout<<x<<endl;//cout<<a<<endl;
                        for(int i=2; i<a;i++){if(x%i==0.000000000000000000000000000000000000000000000000000000000000000) {n=i; return true;}}
                        return false;
                           }


int main(){
  ll x=65535;   string str; int a=0;
  //ll b=pow_longlong(5,15); cout<<b;

ifstream f("io.txt"); ofstream ff; ff.open("ot.txt");
getline(f,str);
 //cout<<x;
  //cout<<bar;
ff<<"Case #1:"<<endl;
 for(;x>32767;x--) {ll m2=0,m3=0,m4=0,m5=0,m6=0,m7=0,m8=0,m9=0,m=0; ll d=0,d1=0,d2=0,d3=0,d4=0,d5=0,d6=0,d7=0,d8=0,d9=0;
                 //cout<<x;

                bitset<16> bar (x); if (bar[0]==0) continue;// cout<<bar;

                for(int i=0; i<16;i++){
                m2+=bar[i]*ceil(pow(2, i));} if (!dv(m2,d2)) continue;

                 for(int i=0; i<16;i++){
                m3+=bar[i]*ceil(pow(3, i));}  if (!dv(m3,d3)) continue;

                 for(int i=0; i<16;i++){
                m4+=bar[i]*ceil(pow(4, i));} if (!dv(m4,d4)) continue;

               for(int i=0; i<16;i++){
                m5+=bar[i]*ceil(pow (5, i));} if (!dv(m5,d5)) continue;//cout<<"asdas";

                 for(int i=0.0; i<16;i++){
                 m6+=bar[i]*ceil(pow (6.0, i));}  if (!dv(m6,d6)) continue;

                for(int i=0; i<16;i++){
                m7+=bar[i]*ceil(pow (7, i));}  if (!dv(m7,d7)) continue;

                 for(int i=0; i<16;i++){
                m8+=bar[i]*ceil(pow (8, i));} if (!dv(m8,d8)) continue;

                 for(int i=0; i<16;i++){
                m9+=bar[i]*ceil(pow (9, i));} if (!dv(m9,d9)) continue;
                 bitset<16> bar2(m2);
                 for(int i=0; i<16;i++){
               m+=bar2[i]*ceil(pow (10, i)); } ; if (!dv(m,d)) continue;
                a++;

                bitset<16> bar1 (x);

                ff<<bar1<<" "<<d2<<" "<<d3<<" "<<d4<<" "<<d5<<" "<<d6<<" "<<d7<<" "<<d8<<" "<<d9<<" "<<d<<endl;
                if (a==50) break;
                }









  //std::bitset<16> baz (std::string("0101111001"));
  return 1;
}
