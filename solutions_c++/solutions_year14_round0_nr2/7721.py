#include <fstream>
#include <iostream>
#include<iomanip>
using namespace std;
int main()
{
        long double c,x,f,div=2,ans1,ans2,temp;
        long test;
        int k=0;

        ifstream fp;
        ofstream op;

        fp.open("B-large.in");
        op.open("output.in");
        fp>>test;


    while(test>0)
    {
        fp>>c;
        fp>>f;
        fp>>x;

        div=2;

        ans1=x/2;
        ans2=0;
        while(1)
        {
            temp=c/div;
            div+=f;
            temp+=x/div;
            temp+=ans2;

            if(temp<ans1)
            {
                ans1=temp;
                temp-=x/div;
                ans2=temp;
            }
            else
                break;

        }
        op<<"Case #"<<k+1<<": "<<setprecision(20)<<ans1<<endl;
        test--;
        k++;
    }
}
