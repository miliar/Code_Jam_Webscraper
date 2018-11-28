#include <iostream>
#include<cstdio>
#include<iomanip>
#include<cstring>
using namespace std;
int T , thenumberofholytestcases=0 ;
double thegreattiger,C,F,D,X,A;
int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>T;
    while(T--){
        thenumberofholytestcases++;
        thegreattiger=X=0.0; A=2.0;
        cin>>C>>F>>D;
        while( C/A + D/(F+A) < D/A ){
            thegreattiger+=C/A;
            A+=F;
        }
        printf("Case #%d: ",thenumberofholytestcases);
        thegreattiger+=D/A;
        cout<<fixed<<setprecision(7)<<thegreattiger<<endl;
    }
}