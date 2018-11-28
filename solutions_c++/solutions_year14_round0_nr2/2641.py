#include<iostream>
#include<cstdio>
using namespace std;
double calculate(double c,double f,double x,long long int n){
    double time;
    time=x/(2+(n*f));
    for(int i=0;i<n;i++){
        time+=(c/(2+(i*f)));
    }
    return time;
}
int main(){
    freopen("1.in", "r", stdin) ;
    freopen("1.out", "w", stdout) ;
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        double c,f,x;
        cin>>c>>f>>x;
        double temp1,temp2,temp3,ans;
        temp1=(-(x*f))+(2*c);
        temp2=f*c;
        cout<<"Case #"<<i<<": ";
        if(temp1<0){
           long long  int n=(-temp1)/temp2;
            ans=calculate(c,f,x,n);
            printf("%.7lf",ans);
        }
        else{
            ans=calculate(c,f,x,0);
            printf("%.7lf",ans);    
        }
        cout<<"\n";  
    }
} 
