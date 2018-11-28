/*
* abeakkas
* Google CodeJam 2015 - Round 2
* Problem B
* Game after game after game...
*/
#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <utility>

typedef long long int ll;

#define pr pair<ll,ll>
#define vpr vector<pair<ll,ll> >

//DEBUGGING
#define _s cout<<
#define _d <<" "<<
#define _e <<endl;

//(int *)calloc(1000000,sizeof(int));
//(int *)malloc(1000000*sizeof(int));

using namespace std; 
ifstream fin ("B.in");
ofstream fout ("B.out");

int main(){
    int T;
    fin>>T;
    for(int iT=1;iT<=T;iT++){
        fout<<setprecision(20);
        int N;
        double V,X;
        fin>>N>>V>>X;
        double R[100],C[100];
        for(int i=0;i<N;i++) fin>>R[i]>>C[i];
        if(N==1){
            if(abs(C[0]-X)<0.00000001) 
            fout<<"Case #"<<iT<<": "<<(V/R[0])<<endl;
            else
            fout<<"Case #"<<iT<<": IMPOSSIBLE"<<endl;
            continue;
        }
        if(N==2){
            if(abs(C[0]-X)<0.00000001 && abs(C[1]-X)<0.00000001)
            fout<<"Case #"<<iT<<": "<<(V/(R[0]+R[1]))<<endl;
            else if(abs(C[0]-X)<0.00000001) 
            fout<<"Case #"<<iT<<": "<<(V/R[0])<<endl;
            else if(abs(C[1]-X)<0.00000001) 
            fout<<"Case #"<<iT<<": "<<(V/R[1])<<endl;
            else if((C[0]<X && C[1]<X) || (C[0]>X && C[1]>X))
            fout<<"Case #"<<iT<<": IMPOSSIBLE"<<endl;
            else {
                 double a=V*(X-C[0])/R[1]/(C[1]-C[0]);
                double b=V*(C[1]-X)/R[0]/(C[1]-C[0]);
            fout<<"Case #"<<iT<<": "<<max(a,b)<<endl;
            }
            continue;
        }
        double coldR=0,coldC=0;
        double hotR=0,hotC=0;
        int flag1=0,flag2=0;
        for(int i=0;i<N;i++){
            if(C[i]<X){
                coldR+=R[i];
                coldC+=R[i]*C[i];
                flag1=1;
            }else{
                hotR+=R[i];
                hotC+=R[i]*C[i];
                flag2=1;
            }
        }
        if(flag1==1)
          coldC/=coldR;
        if(flag2==1)
          hotC/=hotR;
        if((flag1==1 && X-coldC<.00000000001) && (flag2==1 && hotC-X<.00000000001)){
            fout<<"Case #"<<iT<<": "<<(V/(coldR+hotR))<<endl;
            continue;
        }
        if((flag1==1 && X-coldC<.00000000001)){
            fout<<"Case #"<<iT<<": "<<(V/(coldR))<<endl;
            continue;
        }
        if((flag2==1 && hotC-X<.00000000001)){
            fout<<"Case #"<<iT<<": "<<(V/(hotR))<<endl;
            continue;
        }
        if(flag1*flag2==0){
            fout<<"Case #"<<iT<<": IMPOSSIBLE"<<endl;
            continue;
        }
        double a=V*(X-coldC)/hotR/(hotC-coldC);
        double b=V*(hotC-X)/coldR/(hotC-coldC);
        if(a>b) fout<<"Case #"<<iT<<": "<<a<<endl;
        else fout<<"Case #"<<iT<<": "<<b<<endl;
    }
	return 0;
}
