#include<iostream>
#include<iomanip>

using namespace std;
int main(){
   int tcase;
   cin>>tcase;
   for(int i=0;i<tcase;i++)
    {
     double cook=0;
     double c;
     double f;
     double x;
     double rate=2;
     double time=0;
     cin>>c;
     cin>>f;
     cin>>x;
     int count=0;
     while(c/rate+x/(rate+f)<x/rate){
       time+=c/rate;
       rate+=f;
     }
       time+=x/rate;
       cout<<"case #"<<i+1<<":"<<" ";
       cout<<setprecision(7)<<time<<endl;
    }
}
