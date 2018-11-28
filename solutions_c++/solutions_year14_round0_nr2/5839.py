#include<iostream>
#include<iomanip>
#include<vector>
#include<cstdio>
using namespace std;
int main(){
    int t,cas=0;
    cin>>t;
    while(t--){
        double now=2;
        double c,f,x;
        double time=0;
        //cin>>c>>f>>x;
        scanf("%lf %lf %lf",&c,&f,&x);
        while(x/now > x/(now+f)+(c/now)){
            time+=c/now;
            now+=f;
        }
        time+=x/now;
        cout<<"Case #"<<++cas<<": "<<fixed<<setprecision(7)<<time<<endl;
    }
}
