#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<fstream>
using namespace std;
#define N 5
double c, f, x, s;
int ju()
{
    double temp = (c/s) + (x/(s+f));
    if(x/s > temp)
        return 1;
    else
        return 0;
}
int main()
{
    int k,time;
  //  ifstream cin("G:\\B-large.in");
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-large.out","w",stdout);

    scanf("%d",&k);
    string ans[N]= {"Case #",": "};
    for(time = 1; time <= k; time++)
    {
        s= 2.0;
        double tot = 0,tt = 0;
        cin>>c>>f>>x;
        while(ju())
        {
            tt += c/s;
            s += f;
        }
        tt += x/s;
        printf("Case #%d: %.7lf\n",time,tt);
    }
    return 0;
}
