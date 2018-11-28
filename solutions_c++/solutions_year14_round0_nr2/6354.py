#include<iostream>
#include<cmath>
#include<ios>
#include<vector>
#include<algorithm>
#include<fstream>

using namespace std;
typedef long long ll;
typedef long double ld;

int main(){
    ios_base::sync_with_stdio(0);
    ifstream in;
    ofstream ou;
    ou.open("B-large.out",ofstream::out);
    in.open("B-large.in",ifstream::in);
    int T;
    in>>T;
    ou.precision(7);
    ou.setf(ios::fixed,ios::floatfield);
    for(int ii=0;ii<T;++ii)
    {   
        ou<<"Case #"<<ii+1<<": ";
        ld c,f,x;
        in>>c>>f>>x;
        if(c>x)
        {
            ou<<x/2.0<<"\n";
            continue;
        }
        ld cc = c, time = c/2.0, cr = 2.0;
        while(true)
        {
            if((x-cc)/cr > (x-cc+c)/(cr+f))
            {
                cr+=f;
                cc = cc - c;
            }
            if(cc+c >=x)
            {
                time+=(x-cc)/cr;
                break;
            }
            else
            {
                cc+=c;
                time+=(c/cr);
            }
        }
        ou<<time<<"\n";
    }
    ou.close();
    in.close();
}

            
 
