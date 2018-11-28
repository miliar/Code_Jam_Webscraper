#include<iostream>
#include<cstdio>
using namespace std;
double func(double c,double f,double x,double growth){
    double prev,curr;
    prev=(c/growth)+(x/(growth+f));
    growth+=f;
    if(prev>(x/(growth-f)))
        return (x/(growth-f));
    do{
        curr=(prev-(x/growth))+(c/growth)+(x/(growth+f));
        growth+=f;
        if(prev<curr)
            break;
        else
            prev=curr;
    }while(1);
    return prev;
}
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    double c,f,x;
    cin>>t;
    int i=1;
    while(t--){
        cout<<"Case #"<<i++<<": ";
        cin>>c>>f>>x;
        printf("%.7f\n",func(c,f,x,2.0000000));
    }
}
