#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main(){

double sor=0.0,nost=2.0,cot,fuck,xot;
 long long int tok,zos=0;
                                     scanf("%lld",&tok);


while(tok--){

sor=0.0;
zos++;
nost=2.0;
scanf("%lf %lf %lf",&cot,&fuck,&xot);

while(xot/nost>(  xot/(nost+fuck) +cot/nost)){
//cout<<s<<'\t';
sor+=cot/nost;
nost+=fuck;
}
sor+=xot/nost;

printf("Case #%lld: %.7lf\n",zos,sor);
}
return 0;
}
