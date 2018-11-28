#include<iostream>
#include<iomanip>
#include<cstdio>
#include<fstream>
#include<cmath>
using namespace std;
int main()
{
    int t,l=1;
    ifstream cin("B-small.in");
	ofstream cout("b.txt");
    cin>>t;
    while(t--){
        double c,f,x,t=0,fe=2;
        cin>>c>>f>>x;
        do{
            t+=(c*1.0/fe);
            if((x-c)*1.0/fe >= x*1.0/(fe+f)){
                fe+=f;
            }
            else{
                t+=((x-c)*1.0/fe);
                break;
            }
        }
        while(1);
        cout<<"Case #"<<l<<": ";
        cout<<setprecision(7)<<fixed;
        cout<<t<<endl;
        l++;


    }

}






















