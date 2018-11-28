#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;
int main ()
{

//    ofstream output;
//    ifstream input;
//    input.open("input.in");
//    output.open("output.out");

    double C, F, X, speed, last=100001, curr=100000, timt;
    int inst, t;
    cin>>t;

    for (int g=0;g<t;g++)
    {
        cin>>C>>F>>X;
        speed=2;
        inst=0;
        last=100001;
        curr=X/2;
        timt=0;
        while (last>curr)
        {
            last=curr;
            timt=timt+C/speed;
            speed+=F;
            curr=timt+X/speed;
            //cout<<last<<" "<<curr<<endl;
        }
        cout<<"Case #"<<g+1<<": "<<setprecision(7)<<std::fixed<<last<<endl;


    }
    return 0;
}
