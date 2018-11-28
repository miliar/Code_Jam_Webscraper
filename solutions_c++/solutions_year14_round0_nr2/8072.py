#include<iostream>
#include<stdio.h>
using namespace std;

double Min(double a, double b)
{
    if(a<b) return a;
    else return b;
}





int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("b.txt", "w", stdout);

    double C, F, X, n, ret1, ret2,sum;
    int T, kase=0;
    cin>>T;
    double MM, temp;
    while(T--)
    {
        n=0;
        sum=0;
        cin>>C>>F>>X;
        MM=X/2.0;

        while(true)
        {
            ret1 = X/(2.0+F*n);
            ret2 = C/(2.0+F*n) + X/(2.0+F*(n+1.0));
            //cout<<ret1<<" "<<ret2<<endl;
            //getchar();

            if(ret1<ret2)
            {
                sum+=ret1;
                break;
            }
            else
            {
                sum+= ( C/(2+F*n) );
            }
            n+=1.0;
            //cout<<"Sum: "<<sum<<endl;
        }
        printf("Case #%d: %0.7lf\n", ++kase, sum);
    }


}
