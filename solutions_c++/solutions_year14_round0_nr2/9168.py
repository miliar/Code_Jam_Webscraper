#include <iostream>
#include <fstream>
#include <iomanip> 
using namespace std;

int main() {
    // your code goes here
    ifstream cin("input.txt");
        double c, f, x;
        int t;
        cin>>t;
        for (int i=0; i<t; i++)
        {
                cin>>c>>f>>x;
                bool done = 0;
        double tot =0, curc = 2;
        while(!done){
            double val1, val2;
            val1 = x/curc;
            val2 = (c/curc) + x/(curc+f);
            if(val1<val2)
            {

                done = 1;
                tot = tot+val1;
            }
            else{
                 
                tot=tot+c/curc;
                curc+=f;
            }
        }
        cout<<"Case #"<<fixed<<setprecision(7)<<i+1<<": "<<tot<<endl;
        }
        return 0;
}