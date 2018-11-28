#include <iostream>
#include <stdlib.h>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <stdlib.h>
using namespace std;

/*double func(double c, double f, double x) {
    double rate=2.0;
    int num=0;  //number of farms to buy
    double ans=x/rate; //time
    double temp=0;  //time
    double purana=0;
    double rate1=rate;
    while(1) {
        for(int i=0; i<num; i++) {
            temp=temp+(c/rate);
            rate=rate+f;
        }
        temp=temp+(x/rate);
        num++;
        if(temp>ans) {
            return ans;
        }
        ans=temp;
        rate=2.0;
        temp=0;
    }
}*/

double func(double c, double f, double x) {
    double rate=2.0;
    int num=1;  //number of farms to buy
    double ans=x/rate; //time
    double temp=0;  //time
    double temp1=0;
    while(1) {
        /*for(int i=0; i<num; i++) {
            temp=temp+(c/rate);
            rate=rate+f;
        }*/
        temp=temp1+(c/rate);
        temp1=temp;
        rate=rate+f;
        temp=temp+(x/rate);
        num++;
        if(temp>ans) {
            return ans;
        }
        ans=temp;
        // rate=2.0;
        temp=0;
    }
}

int main() {
    ofstream outputFile("output.txt");
    // vector<double> out(0);
    std::ifstream input("B-large.in");
    int cases;
    input >> cases;  // reads a number from somefile.txt
    for(int i=0; i<cases; i++) {
        double C, F, X;
        input>>C>>F>>X;
        outputFile<<"Case #"<<i+1<<": "<<setprecision(15)<<func(C, F, X)<<endl;
    }
    return 0;
}
