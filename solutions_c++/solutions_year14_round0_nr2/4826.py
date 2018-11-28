#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cmath>
#include<string.h>
#include<ctime>
#include<set>
#include<vector>
#include<stack>
#include<queue>
#include <cstdio>
//#define F first
//#define S second
//#define mp make_pair
#define inf 1000*1000*1000
#define mod 1000000007
double delta=0.0000001;
using namespace std;
double go(double c, double f, double x, double v)
{
    //cout<<c<<" "<<f<<" "<<x<<" "<<v<<" "<<(double)(x) / v<<" "<<(double) (x) / (v + f) + (double)(c) / v<<endl;
    if((double)(x) / v < (double) (x) / (v + f) + (double)(c) / v)
        return (double)(x) / v;
    return min(go(c, f, x, v + f) + (double)(c) / v, (double)(x) / v);
}
double t, ind, c, f, x;
int main()
{
    ifstream cin("B-small-attempt1.in");
    ofstream cout("B-small-attempt1.out");
    cin>>t;
    while(t--)
    {
        ind ++;
        cin>>c>>f>>x;
        cout<<"Case #"<<(int)ind<<": ";
        cout.precision(7);
        cout<<fixed<<go(c, f, x, 2)<<endl;
    }
}
