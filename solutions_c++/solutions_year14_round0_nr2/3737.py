#include<iostream>
#include<cstdlib>
#include<vector>
using namespace std;
int main(){
    freopen("test3.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int n;
    cin>> n;
    for(int j=0;j<n;j++){
        double C,F,X,cp=2.0,cS=0,mn=1000000000.000000000;
        cin>>C>>F>>X;
        while(true){
            if(mn > ( (X/cp) +cS ) )
                mn=X/cp + cS;
            else
                break;
            cS+=C/cp;
            cp+=F;
        }
        cout.precision(15);
        cout<<"Case #" << j+1 << ": "<< mn <<endl;
    }
return 0;
}
