/*
C F X
//we need to reach to X in minimum time. Every time we spend C speed = speed + F;
if time to X with current speed < time spent to buy farm + time spent to reach X with new speed the STOP
else
 buy Farm and continue.
*/

#include<iostream>
#include<stdio.h>
#include<vector>
#include<iomanip>
#include<cstring>
#include<conio.h>

using namespace std;

int cont = 0;
double speed = 2;

double calculateTime( double c, double f, double x){
    cont = 0;
   // double time = 0.000;

    double timeX = x/speed;


    double timeC = c/speed;

    double newTimeX = x/(speed+f);

    //cout<<"timeX = "<<timeX<<" and timeC+ newtimeX = "<<timeC+ newTimeX<<endl;

    if(timeX > timeC + newTimeX){
            cont = 1;
            speed = speed + f;

            return timeC;

    }

    return timeX;

}


int main(){

    freopen("inputp2.in", "r", stdin);
    freopen("p2Output.txt", "w", stdout);

    int t;
    cin>>t;

    for(int k=0; k<t; k++){//while(t--){
        speed = 2;
        cont = 0;

        double c, f, x;
        cin>>c>>f>>x;


        double time = 0.00000;

        do{
                double y = calculateTime(c, f, x);
                //cout<<y<<endl;
                time = time + y;
        }while(cont == 1);

        cout<<"Case #"<<k+1<<": "<<setprecision(7)<<fixed<<time<<endl;



    }

}
