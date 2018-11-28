#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
//#include <ctime>
#include <map>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(7);
    double c,f,x;
    int t;
    cin>>t;
    for (int k=1;k<=t;k++)
    {
        cout<<"Case #"<<k<<": ";
        cin>>c>>f>>x;
        double count=2.0;
        double cur=0.0;
        double min=x/2;
        double time=0.0;
        while (true)
        {
            time=time+c/count;
            count=count+f;
            if (min>(time+x/count))
            {
                min=(time+x/count);
            }
            else if (x/count<(c/count+x/(count+f)))
            break;
        }
  //      cout<<time<<endl;
    //    cout<<count<<endl;
        cout<<min<<endl;
    }
    return 0;
}
