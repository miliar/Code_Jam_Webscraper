#include <fstream>
#include <iostream>

#define EPS 1e-7

using namespace std;

ifstream fin("B-small-attempt3.in");
//ifstream fin("cookiein.txt");
ofstream fout("cookieout.txt");

double farm, farmRate, limit;

bool isGreater(double a, double b){
    return a > b - EPS;
}

double smaller(double a, double b){
    if(isGreater(a,b)) return b;
    return a;
}

void solveCase(int caseNo);
double getTime(int purchases);

int main(int argc, char* argv[]){
    int t;
    fin >> t;
    for(int i = 0; i < t; i++){
        solveCase(i + 1);
    }
    fin.close();
    fout.close();
    return 0;
}

void solveCase(int caseNo){
    fin >> farm >> farmRate >> limit;
    int purchases = 0;
    double old = limit / 2;
    double temp = getTime(++purchases);
    while(isGreater(old,temp)){
        old = temp;
        temp = getTime(++purchases);
    }
    /*double old = limit/2;
    for(int i = 1; i < 2001; i++){
        old = smaller(old,getTime(i));
    }*/
    fout.precision(7);
    fout << "Case #" << caseNo << ": " << fixed << old << '\n';
    return;
}

double getTime(int purchases){
    double time = 0, rate = 2;
    for(int i = 0; i < purchases; i++){
        time += farm/rate;
        rate += farmRate;
    }
    return time + limit/rate;
}

