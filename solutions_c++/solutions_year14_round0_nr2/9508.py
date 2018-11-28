#include<iostream>
#include<iomanip>
#include<cstdio>

using namespace std;

long double timeX(long double C, long double F, long double x)
{
    if(x == 0)
        return 0;
    else
    {
        return timeX(C, F, x-1) + (C/(2 + F*(x - 1)));
    }
}

void print(float *a, int t)
{
    for(int i=0; i<t; i++)
        cout<<a[i]<<"\t";
    cout<<endl;
}

int main(void)
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("result.in", "w", stdout);
    int t;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        long double C, F, X;
        long double a, b, c[2];

        cin>>C;
        cin>>F;
        cin>>X;

        int j;
        for(j=0; j<2; j++)
        {
            a = timeX(C, F, j);
            b = X/(2+(F*j));
            c[j] = a + b;
        }

        while(c[1] < c[0])
        {
            a = timeX(C, F, j);
            b = X/(2+(F*j));
            c[0] = c[1];
            c[1] = a + b;
            j++;
        }
        cout<<"Case #"<<i+1<<": "<<fixed <<setprecision(7)<<c[0]<<endl;
    }

    return 0;
}
