#include<iostream>
#include<cstring>
#include<fstream>
#include<cstdio>
using namespace std;
int main(){
    ifstream cin("B-large.in");
    ofstream cout("out.out");
    //freopen("out.txt", "w" ,stdout)
    int T,apple = 1;
    cin>>T;
    while(T--){
        double c,f,x,rate = 2.0,time = 0;
        cin>>c>>f>>x;
        while(x / rate > c / rate + x /(rate + f)){
            time += c / rate;
            rate += f;
        }
        time += x / rate;
        cout<<"Case #"<<apple++<<": ";
        cout.precision(7);
        cout.setf(ios::fixed);


        //printf("%.7f\n",time);
        cout<<time<<endl;

    }

    return 0;
}
