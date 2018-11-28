#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int T;
    cin >> T;
    for (int i=1; i<=T; i++)
    {
        double r,t;
        cin >> r;
        cin >> t;
        double b=2.0*r+3.0;
        double value=(-b+sqrt((b)*(b)-8*(2.0*r+1-t)))/4.0;
        int num=int(value)+1;
        //cout << value << endl;
        cout << "Case #" << i << ": "<<num<<endl; 
    }
    return 0;
}
