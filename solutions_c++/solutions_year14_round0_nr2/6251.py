#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <cstring>
#include <iomanip> 
using namespace std;

//function declaraions

int main(){

    string fname = "large";
    freopen((fname+".in").c_str(), "r", stdin);
    freopen((fname+".out").c_str(), "w", stdout);// ------- needed to output to file

    //number of cases to follow
    int cases;
    scanf("%d", &cases);
    cout << fixed;
    cout << setprecision(7);

    for (int i = 0; i < cases; ++i) {
        //values about each case
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f,&x);
        // logic


        bool win = false;
        double currentRate = 2.0;
        double t = 0;
        double balance = 0;

        while (win == false){
            double t2win = x/currentRate;
            double t2winaddc = (c/currentRate)+((x)/(currentRate + f));
            //cout<<"c "<<c<<" f "<<f<<" x "<<x<<endl;
            //cout<<"t2win "<<t2win<<" t2winaddc "<<t2winaddc<<endl;
            if (t2win<=t2winaddc){
                t+=t2win;
                win=true;
            }else{
                t+=c/currentRate;
                currentRate+=f;
            }
            //cout<<"t = "<<t<<" CR = "<<currentRate<<endl;
            //win=true;
        }

        // answer
        printf("Case #%d: ", i+1);
        cout<<t<<endl;

    }

    return 0;
}
