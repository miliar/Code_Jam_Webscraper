#include<iostream>
#include<cstdio>
#define SIZE 100001
using namespace std;
double f[SIZE];
int main()
{
    double C,F,X;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B.txt","w",stdout);
    int cas;
    cin>>cas;
    for(int q=1;q<=cas;q++)
    {
        cin>>C>>F>>X;
        double sol = -1,t;

        for(int i=0;i<SIZE;i++)
        {
            if(i==0)
                f[i] =0;
            else
                f[i] = f[i-1] + C/(2+(i-1)*F);
            t =  f[i] +X/(2+i*F);
            if(sol > 0 && t > sol+1)break;
            if(sol < 0 || sol > t)
                sol = t;
        }
        cout<<"Case #"<<q<<": ";
        printf("%.7lf\n",sol);
    }
    return 0;
}
