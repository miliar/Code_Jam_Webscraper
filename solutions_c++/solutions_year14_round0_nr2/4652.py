#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
void cal(double v, double c, double f, double x, double &result){
    double t1 = x/v;
    double t2 = c/v + x/(v+f);
    if(t1 < t2){
        result += t1;
    }
    else{
        result += c/v;
        cal(v+f, c, f, x, result);
    }
}
int main()
{
    ofstream fout;
    fout.open("out.txt");
    ifstream fin;
    fin.open("B-small-attempt1.in");
    int T;
    int caseNum = 0;
    fin>>T;
    double C, F, X;
    while(caseNum < T){
        caseNum++;
        fin>>C>>F>>X;
        double result = 0;
        cal(2, C, F, X, result);
        fout<<"Case #"<<caseNum<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<result<<endl;        
    }
    system("pause");
    return 0;
}
