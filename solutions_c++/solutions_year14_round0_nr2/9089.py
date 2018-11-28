#include<fstream>
#include<iostream>
#include<cmath>
using namespace std;


ofstream fout ("Sol00.txt");
ifstream fin ("Sol00.in");
double C,F,X;
int T,c;
double res;
void read(){
    fin >> C >> F >> X;
}

void eval(){
    res=X/C-1-2/F;
    int num=ceil(res);
    //cout << res << endl;
    double res0=0;
    for(int i=0;i<num;i++){
        res0+=C/(F*i+2);
    }
    //cout << res0 << endl;
    if(num<=0) {res=X/2;}
    else{
        res=X/(num*F+2);
        res+=res0;
    }
}


void write(){
    c++;
    fout << "Case #" << c << ": " ;
    fout << res << endl;
}


int main(){
    fin >> T;
    fout.unsetf(std::ios::floatfield);
    fout.precision(7);
    fout.setf(ios::fixed, ios::floatfield);
    while(T--){
        read();
        eval();
        write();
    }
    return 0;

}
