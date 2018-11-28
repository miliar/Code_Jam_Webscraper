#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
    long int counter=0,yo;
    cin>>yo;
    double arr[yo];
    while(yo--){
    double x,y,a,tim,b,c,f,timm,curr=0.000000,rate=2.000000;
    tim=0.000000;
    cin>>c>>f>>x;
    while(1){
        timm=c/rate;
        if(((x) / rate ) < (( x/(rate+f) )+ timm ) ){
            tim=tim+(x / rate );
            break;}
        tim=tim+(timm);
        rate+=f;
    }
    arr[counter]=tim;
    counter++;
    printf("Case #%d: %.7lf\n",counter,tim);
}
for(long int i=0;i<yo;i++){
    printf("Case #%d: %.7lf\n",i+1,arr[i]);
}
}
