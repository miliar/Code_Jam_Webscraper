#include <cstdlib>
#include <iostream>
#include <bits/stdc++.h>



using namespace std;
#define decimal double

decimal function_(decimal &c,decimal &f,decimal &x,decimal &acumTime,decimal &cps){
    if((acumTime+c/cps+x/(cps+f))>(acumTime+x/(cps)) ){
        return (acumTime+x/(cps));
    }else {
            acumTime+=c/cps;
            cps+=f;
            return function_(c,f,x,acumTime,cps);
    }

}

int main(int argc, char *argv[])
{
    ifstream cin("B-large.in");
//    ifstream cin("entrada.txt");
    ofstream cout("A-small-attempt2.txt");

    long long int case_=0;
    decimal c=0,f=0,x;
    decimal acumTime,cps,r;
    cin>>case_;
    for (int k=1;k<=case_;k++){
            cin>>c>>f>>x;
            acumTime=0;
            cps=2;
            while(true){
                if((acumTime+c/cps+x/(cps+f))>(acumTime+x/(cps)) ){
                    r=(acumTime+x/(cps));
                    break;
                }else {
                        acumTime+=c/cps;
                        cps+=f;
                        //return function_(c,f,x,acumTime,cps);
                }

            }
            //r=function_(c,f,x,acumTime,cps);
            cout<<"Case #"<<k<<": ";
            cout << setiosflags(ios::fixed | ios::showpoint) << setprecision(7);
            cout<<r<<endl;

    }


    return 0;
}
