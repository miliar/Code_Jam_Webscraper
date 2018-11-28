#include<iostream>
#include<stdlib.h>
#include<iomanip>
using namespace std;

int main(){
double tfinal=0.0,F,C,X,tim=0.0,r=2.0;
int t,T;
cin>>T;
for (t=1; t<=T; t++){
        tfinal=0.0;
        r=2.0;
        cin>>C>>F>>X;
while((X/r)>(C/r)+X/(r+F))
      {tfinal+=C/r;
      r+=F;
      }
      tfinal+=X/r;
      cout<<"Case #"<<setprecision(11)<<t<<": "<<tfinal<<"\n";
      }


return 0;
}
