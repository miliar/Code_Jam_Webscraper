#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <locale>
#include <iomanip>
#include <cctype>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>

#define pi 3.1415926535

using namespace std;

int main(void)
{
    ifstream cin("A-small-attempt0.in");
    ofstream cout("A-small-attempt0.out");
    long long int T,i,j,k;
    long long int r,mili,rings;
    cin>>T;
    for(k=0;k<T;k++)
    {
        cin>>r>>mili;
        rings=0;
        long long int taken=(r+1)*(r+1)-r*r;
        //cout<<mili<<" ";
        //cout<<taken;
        while(mili-taken>=0)
        {
            //cout<<(r+1)*(r+1);
            //r+=2;
            //rings++;
            //cout<<mili-taken<<"\n";
            mili=mili-taken;
            r+=2;
            rings++;
            taken=(r+1)*(r+1)-r*r;
        }
        cout<<"Case #"<<k+1<<": "<<rings;
        cout<<"\n";
    }
    return 0;
}
