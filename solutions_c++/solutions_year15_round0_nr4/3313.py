#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <map>

using namespace std;

int main() {
    int zc;
    cin>>zc;
    for(int tc=1;tc<=zc;tc++)
    {
        int X,R,C;
        cin>>X>>R>>C;

        if(X==1)
            cout<<"Case #"<<tc<<": "<<"GABRIEL"<<endl;
        if(R*C<X)
        {
            cout<<"Case #"<<tc<<": "<<"RICHARD"<<endl;
            continue;
        }
        if(X==2)
        {
            if(R*C%2==0)
                cout<<"Case #"<<tc<<": "<<"GABRIEL"<<endl;
            else
                cout<<"Case #"<<tc<<": "<<"RICHARD"<<endl;
        }
        if(X==3)
        {
            if((R==3||C==3)&&R*C!=3)
                cout<<"Case #"<<tc<<": "<<"GABRIEL"<<endl;
            else
                cout<<"Case #"<<tc<<": "<<"RICHARD"<<endl;

        }
        if(X==4)
        {
            if((R==4||C==4)&&R*C>=12)
               cout<<"Case #"<<tc<<": "<<"GABRIEL"<<endl;
            else
                cout<<"Case #"<<tc<<": "<<"RICHARD"<<endl;
        }

    }
    return 0;
}


