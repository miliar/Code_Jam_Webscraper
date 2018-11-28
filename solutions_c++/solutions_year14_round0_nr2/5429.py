/*N*/
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<numeric>
#include<iomanip>
#include<string>
#include<vector>
#include<queue>
#include<set>
#define N 1010

using namespace std;
int a[N];

int main()
{
    int t;
    cin>>t;
    int test=0;
    while(t--)
    {
    	test++;
        double c,f,x;
        double prev= 0, current= 0, rate= 2;
        cin>>c>>f>>x;
        prev= x/rate;
        while(1)
        {
            //cout<<prev<<endl;
            current= c/rate+ prev- x/rate;
            rate+= f;
            current+= x/rate;

            //end
            if(current>= prev)
                break;
            else
                prev= current;
        }
        cout<<"Case #"<<test<<": "<<setprecision(7)<<fixed<<prev<<endl;
    }

    return 0;
}
