#include<iostream>
using namespace std;
int choose(float c, double f, double cur, double x, double t)
{
    double i1, i2;
    i1 = (x-t)/cur;
    i2 = x/(cur+f);
    if( i2<i1)
        return 1;
    else
        return 0;
}
int main()
{
    int t, l;
    double c,f,x, tot , cur, time,a;
    cin>>t;
    for(int i = 0; i < t; i++)
    {
        tot = 0.0;
        time = 0.0; cur = 2.0;
        cin>>c>>f>>x;
        while(tot < x)
        {
            if(tot < c)
            a = (c-tot)/cur;
            time = time+a;
            cout<<time<<endl;
            tot = c;
            l = choose(c,f,cur,x,tot);
            cout<<l<<endl;
               if(l)
                {
                    cur = cur + f;
                    tot = 0.0;
                }
                else
                {
                time = time - a;
                a =  x/cur;
                time = time +a;
                break;
                }
        }
            cout<<"Case #"<<i+1<<":"<<fixed<<time<<endl;
    }
return 0;
}
