#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <sstream>
#include <fstream>
#include <math.h>
#include <cmath>
#include <vector>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <stdlib.h>
#include <iomanip>
#include <deque>
#include <list>
#include <cctype>
#include <utility>

using namespace std;


const double PI = 2 * acos (0);
/*
3
1 4
10 120
100 1000
*/

bool pal(string I)
{
    if(I.length()==1)
    {
        return true;
    }
    else
    {
        if(I.length()%2==0)
        {
            int X=I.length()/2;
            string A=I.substr(0,X), B=I.substr(X);
            //cout<<"Comparando: "<<A<<" y "<<B<<endl;
            if(A==B) return true;
            else return false;
        }
        else
        {
            int X=(I.length()-1)/2;
            string A=I.substr(0,X), B=I.substr(X+1);
            //cout<<"Comparandoimpar : "<<A<<" y "<<B<<endl;
            if(A==B) return true;
            else return false;
        }
    }
}
int main()
{
    //Problem C. Fair and Square

    int T;
    cin>>T;

    for(int i=1; i<=T; i++)
    {
        int counter=0;
        string K;

        unsigned long long int a,b;

        cin>>a>>b;

        for(int k=a; k<=b; k++)
        {
            stringstream C;
            C << k; C >> K;
            //cout<<K<<endl;
            if(pal(K))
            {
              //  cout<<"Entro"<<endl;
                double kk=sqrt(k);
                stringstream D;
                D << kk; D >> K;
                //cout<<kk<<endl<<k<<" Probando "<<(int)kk<<" y "<<kk<<endl;
                if((int)kk==kk)
                {
                  //  cout<<"Entro otra vez"<<endl;
                    if(pal(K))
                    {
                    //    cout<<K<<" Es el mejor"<<endl;
                        counter++;
                    }
                }
            }
        }
        cout<<"Case #"<<i<<": "<<counter<<endl;
    }
    return 0;
}

