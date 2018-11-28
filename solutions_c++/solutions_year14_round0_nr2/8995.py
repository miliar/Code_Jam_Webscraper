#include <iostream>

using namespace std;

/*
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0
*/
double Tc=0, Tmin=0, Tg=0, aux=0, m=0, Tc_2, Tmin_2, Tg_1, Tg_2;
double tMin(double P, double C, double F, double X);
double tMin(double P, double C, double F, double X)
{
    cout.setf(ios::fixed);
    cout.precision(7);

    Tc=C/P;
    Tmin=X/(P+F);

    Tc_2=C/(P+F);
    Tmin_2=X/(P+2*F);

    Tg+=C/P;
    Tg_1=Tg+Tmin;

    Tg_2=Tg+Tc_2+Tmin_2;

    //cout<<P<<" "<<C<<" "<<F<<" "<<X<<endl;
    //cout<<"     Tc="<<Tc<<" "<<"Tmin="<<Tmin<<" Tg1="<<Tg_1<<endl;
    //cout<<"     Tc2="<<Tc_2<<" "<<"Tmin2="<<Tmin_2<<" Tg2="<<Tg_2<<endl;
    //if(Tc+Tg>=Tmin && Tg_1<Tg_2)
    if(Tg_1<Tg_2)
    {
        //cout<<"Tc="<<Tc<<" "<<"Tmin="<<Tmin<<" Tg="<<Tg<<" Tg+Tmin="<<Tg+Tmin<<endl;
        if(Tg+Tmin>aux)
        {
            m=aux;
        }
        else
        {
            m=Tg+Tmin;
        }
        cout<<m<<endl;;
        return m;
    }
    else
    {
        P+=(F);
        tMin(P,C,F,X);
    }
}

int main()
{
    int T;
    double P=2,C,F,X;
    cin>>T;
    for(int x=1; x<=T; x++)
    {

        cin>>C>>F>>X;
        Tg=0;


        cout.setf(ios::fixed);
        cout.precision(0);
        cout<<"Case #"<<x<<": ";

        double minTime=0;
        aux=X/P;
        minTime=tMin(P,C,F,X);
        //cout<<minTime<<endl;
    }
    return 0;
}
