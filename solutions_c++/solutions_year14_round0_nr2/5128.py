#include<iostream>
#include<iomanip>

using namespace std;

int main(){
    int t,T=1;
    double d=100000;
    cout<<d<<endl;
    double c,f,x,f1,f2,time=0;
    cin>>t;
    while(t!=0){
        cin>>c;
        cin>>f;
        cin>>x;
        f1=2;
        f2=f+f1;
        time=0;
        while(1){
            if(c/f1+x/f2 <= x/f1){
                time+=c/f1;
                f1=f2;
                f2+=f;
            }
            else{
                time+=x/f1;
                cout<<"Case #"<<T++<<": "<<fixed<<setprecision(7)<<time<<endl;
                break;
            }
        }
        t--;
    }
    return 0;
}
