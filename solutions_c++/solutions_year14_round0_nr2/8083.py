#include<iostream>
#include <fstream>
#include <iomanip>
#define wait 1
#define factory 2
using namespace std;

ifstream input("input.txt");
fstream output("output.txt");
int decision,tests;
double C,F,X,cookie_production,time;

void COOKIE_MONSTER(){
input >> tests;
output << setprecision(7) << fixed;
for(int i=1;i<=tests;i++){
    input >> C >> F >> X;
    cookie_production = 2;
    time = 0;
    while(decision!=wait){
        if((X/cookie_production) < ((C/cookie_production)+(X/(cookie_production + F))))decision = wait;

        else {
            decision = factory;
            time += (C/cookie_production);
            cookie_production += F;
        }}
        decision = 0;
        time += (X/cookie_production);
        output << "Case #" << i << ": "<<time << "\n";
}}

int main(){
COOKIE_MONSTER();
return 0;
}
