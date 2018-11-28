using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

#define foreach(x, v) for (typeof (v).begin() x=(v).begin(); x !=(v).end(); ++x)
#define For(i,a,b) for (int i=(a); i<(b); ++i)
#define D(x) cout << #x " is " << x << endl
#define pf printf
#define sf scanf
#define loop while
#define print(i) "Case "

int main()
{
    int t,cases=0;
    ifstream myfile;
    FILE *output;
    output=fopen("output2.txt","w");
    myfile.open("B-large.in", ios::in);
    myfile>>t;
    while(t--)
    {
        double c,f,x;
        myfile>>c>>f>>x;
        //pf("%.lf %lf %lf\n",c,f,x);
        double time1,time2,rate=2.0;
        time1=x/rate;

        //while(time1<time2)
        //{
            time2=c/rate+x/(f+rate);
            //rate=f+rate;

            if(time1<time2)
            {
                fprintf(output, "Case #%d: %.7lf\n", ++cases,time1);
                //output<<"Case #"<<++cases<<": "<<time1<<endl;
            }
            else
            {
                double time3=time2;
                double tmp=0;
                do{
                    time2=time3;
                    time3=tmp+c/rate+x/(f+rate);
                    rate=f+rate;
                    tmp=tmp+c/(rate-f);
                }while(time3<=time2);
                //output<<"Case #"<<++cases<<": "<<time2<<endl;
                fprintf(output, "Case #%d: %.7lf\n",++cases,time2);
            }
        //}
    }
    myfile.close();
    fclose(output);
    return 0;
}

