#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

int main()
{
    //freopen("test", "r", stdin);
    freopen("in", "r", stdin);
    freopen("outb", "w", stdout);
    int testCases;
    cin>>testCases;
    for(int testcase=0;testcase<testCases;testcase++)
    {
        int n;
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++)
            cin>>a[i];
        sort(a,a+n);
        /*for(int i=0;i<n;i++)
            cout<<a[i]<<" ";
        cout<<endl;*/
        int min1=a[n-1]+2;
        for(int i=a[n-1];i>0;i--) {
            int min2=i;
            //min2=ceil(double(a[n-1])/div);
            //cout<<"min2="<<min2<<endl;
            for(int j=n-1;j>=0;j--) {
                //cout<<"a[i]/num="<<ceil(float(a[j])/i)<<" ";
                //cout<<min2<<" ";
                if(ceil(double(a[j])/i) > 1)
                    min2+=ceil(double(a[j])/i)-1;
                else
                    break;
            }
            if(min1>min2)
                min1=min2;
            //cout<<endl<<"min1="<<min1<<" "<<" min2="<<min2<<endl;
        }
        cout<<"Case #"<<testcase+1<<": "<<min1<<endl;
    }
    return 0;
}
