#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;


int main()
{
    ifstream input("D.in");
    string const out("D.out");
    ofstream output(out.c_str());

    int i=0,s,j=0,R,C,X;

    input>>s;

    for(i=1;i<=s;i++){
            input>>X;
            input>>R;
            input>>C;

            if(X==1)output<<"Case #"<<i<<": GABRIEL"<<endl;

            if( X==2 && (R*C)%X!=0 ) output<<"Case #"<<i<<": RICHARD"<<endl;
            else if(X==2) output<<"Case #"<<i<<": GABRIEL"<<endl;

            if( X==3 && ( (R*C)%X!=0 || R*C==3 )) output<<"Case #"<<i<<": RICHARD"<<endl;
            else if(X==3) output<<"Case #"<<i<<": GABRIEL"<<endl;

            if(X==4 &&( (R*C)%X!=0 || R*C==4 || R*C==8 )) output<<"Case #"<<i<<": RICHARD"<<endl;
            else if(X==4) output<<"Case #"<<i<<": GABRIEL"<<endl;



    }

    return 0;
}

