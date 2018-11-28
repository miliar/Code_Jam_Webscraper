#include<iostream>
#include<cstdio>
using namespace std;
double t=0.0,cps=2.0;

void solve(int u)
{
    double c,f,x;
    cin>>c>>f>>x;
    //nt,nnt,tf,prod=2;
    //int z=0;
    while(1)
    {
        if(x/cps>c/cps+x/(cps+f)){
            t+=c/cps;
            cps+=f;
        }
        else{
            t+=x/cps;
//        z++;
//        printf("%.7f   t\n",double(t));
//        printf("%.7f   prod\n",double(prod));
//        tf=x/prod;
//        printf("%.7f   tf\n",double(tf));
//        nt=c/prod;
//        printf("%.7f   nt\n",double(nt));
//        nnt=c/(prod+f);
//        printf("%.7f   nnt\n",double(nnt)0);
//        if(tf<x/(prod+f))
//        {
            cout<<"Case #"<<u<<": ";
            printf("%.7f\n", t);
            t=0;cps=2.0;
            return ;
//        }
//        else
//        {
//            t+=nt;
//            prod+=f;
//        }
        }
    }
}
int main()
{
    int t;
    cin>>t;
    int i;
    for(i=1;i<=t;i++)solve(i);
//    solve(1);
    return 0;
}
/*
500.0 4.0 2000.0

*/