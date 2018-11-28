#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int t;
    cin>>t;

    for(int i=0;i<t;i++) {

        double c,f,x;
        double uplynelo=0.0;
        double czas;
        double v=2.0;
        cin>> c >> f >> x;

        bool oplaca=true; //czy sie op³aca budowac

        czas=x/v;

        while(oplaca==true) {
            uplynelo+=c/v;
            if(uplynelo>=czas) break;
            v+=f;
            if((uplynelo+(x/v))<=czas) czas=uplynelo+(x/v);
            else { oplaca=false; break; }
        }
        printf ("Case #%d: %.7f", i+1,czas);
        if((i+1)<t) cout << endl;
    }

    return 0;
}
