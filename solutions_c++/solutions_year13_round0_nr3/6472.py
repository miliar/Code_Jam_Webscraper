#include <iostream>
#include <math.h>
#include <sstream>
using namespace std;

bool palindrom(string s) {
    bool czyjest=true;
    for(int i=0;i<floor(0.5*s.length());i++) {
        if(s[i]!=s[s.length()-1-i]) czyjest=false;
        }
    return czyjest;
    }

int main() {
    int t,i,i2,j,a,b,ile;
    string s,s2;
    cin>>t;
    for(int l=1;l<=t;l++) {
        ile=0;
        cin>>a;
        cin>>b;
        i=ceil(sqrt(a));
        j=floor(sqrt(b));
        while(i<=j) {
            stringstream ss;
            ss << i;
            s=ss.str();
            if(palindrom(s)) {
                stringstream ss2;
                i2=i*i;
                ss2 << i2;
                s2=ss2.str();
                if(palindrom(s2)) ile++;
                }
            i++;
            }
        cout << "Case #" << l << ": " << ile << endl;
        }
    return 0;
    }
