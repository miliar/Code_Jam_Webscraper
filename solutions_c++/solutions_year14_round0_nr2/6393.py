#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main()
{
    ifstream file("B-large.in");
    ofstream o("B-large.out");
    o.precision(10);
    if (!file.is_open())
        cout<<"error";
    long long n;
    string t;
    getline(file,t);
    n = atoi( t.c_str() );

    for(int i=0; i<n; i++) {
        long double c,f,x,time = 0.0;
        file>>c>>f>>x;

        long double p = 2.0,score = 0;
        o<<"Case #"<<i+1<<": ";
        while(1)
        {
            // not buying
            long double time_to_get_x = (x-score)/p;
            //buying
            long double time_to_buy = c/p;
            long double score_to_buy = time_to_buy*p;
            if(score>c) {
                time_to_buy = 0;
                score_to_buy = 0;
                }
            long double time_after_buying_to_get_x = (x-(score-c+score_to_buy))/(p+f);
            long double time_to_get_all = time_to_buy + time_after_buying_to_get_x;

            if(time_to_get_x<time_to_get_all) {
                o<< fixed <<time+time_to_get_x<<endl;
                break;
                }
            else {
                time+=time_to_buy;
                p+=f;
            }
        }
    }
    return 0;
} 
