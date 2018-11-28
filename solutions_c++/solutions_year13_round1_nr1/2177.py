#include<fstream>
#include<string>
#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

#define MAXANS 100000

ifstream fin("A-small-attempt2.in");
ofstream fout("A-small-attempt2.out");


unsigned long long bin(unsigned long long r, unsigned long long t) {
    unsigned long long low = 1, 
                        height = 4294967295, 
                        mid;
    while (low<height) {
        mid = (low+height)/2;
        if (mid*2*r+(2*mid-1)*mid > t)
            height = mid - 1;
        else 
            low = mid + 1;
    }
    mid *= 2;

    while (mid*2*r+(2*mid-1)*mid > t) 
        mid--;

    return mid;
}

int main() {
    int T,c;
    fin>>T;

    for (c=1; c<=T; ++c) {
        unsigned long long r, t;

        fin>>r>>t;
        unsigned long long ans =  bin(r, t);
        

        // output
        fout<<"Case #"<<c<<": ";
    
        fout<<ans;

        fout<<endl;
    }
    return 0;
}
