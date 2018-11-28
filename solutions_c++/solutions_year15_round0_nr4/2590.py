#include<iostream>
#include<string>
#include<sstream>
#include<cmath>
#include<fstream>

#define T_MAX 107

#define For(n) for(int i = 0; i<(n); i++)
#define ForJ(n) for(int j = 0; j<(n); j++)

#define cin input

bool output[T_MAX];

using namespace std;

int main(){
    ifstream input; input.open("D-small-attempt1.in");
    ofstream out; out.open("D-output-small.out");

    int T, X,R,C;
    cin>>T;

    For(T){
        cin>>X>>R>>C;
        //cout<<(X>=7)<<" || ("<<(X>R)<<" && "<<(X>C)<<") || !("<<((R*C)%X == 0)<<" && "<<((R*C)/X>=3)<<")"<<endl;

        output[i] = false;
        if(X>=7 || (X>R && X>C) || ((X/2+X%2)>R || (X/2+X%2)>C) || !(R*C>0 && (R*C)%X == 0 && ((R*C)/X<3 ? X<4 : true))){output[i] = true;}

    }

    For(T){
        out<<"Case #"<<i+1<<": "<<(output[i] ? "RICHARD" : "GABRIEL")<<endl;
    }



}
