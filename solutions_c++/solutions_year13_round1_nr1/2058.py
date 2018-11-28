#include <iostream>
#include<gmpxx.h>
#include<string>

using namespace std;

mpz_class num(const mpz_class &r, const mpz_class t) {
   mpz_class base=r * r;
   mpz_class ev = 0;
   mpz_class odd = 1;
   mpz_class val = 0;
   mpz_class count = 0;
   while(true) {
        val += (2 * r  + (odd + ev) )* (odd -ev);
        //cout<<"VAL:"<<val<<endl;
        if(val > t) {
            return count;
        }
        count++;
        ev += 2;
        odd += 2;
   } 
}

int main() {
    int numTests = 0;
    cin>>numTests;
    for(int i=1; i <= numTests; i++ ) { 
        string radius, paint;
        cin>>radius;
        cin.clear();
        cin.ignore(1);
        cin>>paint;
        mpz_class radiusInt(radius.c_str(),10);
        mpz_class paintInt(paint.c_str(),10);
        //cout<<"R:"<<radiusInt<<"P:"<<paintInt<<endl;
        cout<<"Case #"<<i<<": "<<num(radiusInt, paintInt)<<endl;
    }
    return 0;
}

