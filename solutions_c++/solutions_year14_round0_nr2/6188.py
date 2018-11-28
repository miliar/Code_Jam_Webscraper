#include <iostream>
#include <cstdio>
#include <conio.h>
#include <Math.h>
#include <vector>
#define lli long long int

using namespace std;

double C,F,X;
double solve(){
    double time=0;
    double cost=2.0;
    double aux=0;
    vector<double>maxi;
int cont=0;
maxi.push_back(X/(cost));
    while(cont<=X){

            aux=C/cost;
            time+=aux;
    maxi.push_back(time+X/(cost+F));
    //cout<<"aux: "<<aux<<"   time :"<<time<<"   "<<(X)/(cost+F)<<"  "<<"   costo "<<cost<<endl;
        cost+=F;
        cont++;
        //if(aux*cost>X)break;
    }
    double mmax=maxi[0];
    for(lli i=0;i<maxi.size();i++ ){
        if(maxi[i]<mmax){mmax=maxi[i];}
    }
    //cout<<"aa: "<<C/cost<<endl;
/*
    do{
        aux=C/cost;
        time+=aux;
        cout<<"aa: "<<aux<<"  "<<cost<<endl;
        cost+=F;
       // if(C>X/cost)break;
    }while( time+(C/(cost-F))>=C &&time<=X);
     //cout<<"aa: "<<X/cost<<endl;
     //cout<<"aa: "<<X/(cost-F)<<endl;
     //cout<<"aa: "<<X/(cost+F)<<endl;
        time+=(X/(cost+F));*/
    return mmax;
}


int main()
{
FILE *out;
    out=fopen("out.txt","r+");
    lli t;
    cin>>t;
    for(lli m=1;m<=t;m++){
            cin>>C>>F>>X;
        fprintf(out,"Case #%lld: %.7f\n",m,solve());
    }

    return 0;
}
