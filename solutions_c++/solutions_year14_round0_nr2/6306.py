#include<iostream>

using namespace std;

long double C,F,X;




void do_a_case(int case_no)
{
    long double R=2.0,spend=0.0,T,ctime,ftime;
    cin>>C>>F>>X;
    while(1)
    {
        ctime=X/R+spend;
        T=R+F;
        ftime=C/R+X/T+spend;
        if(ctime<=ftime)break;
        spend+=C/R;
        R+=F;
        /*cout<<ctime<<" : "<<ftime<<endl;
        cin.get();*/
    }
    cout.precision(7);
    cout<<"Case #"<<case_no<<": "<<fixed<<showpoint<<ctime<<endl;

}


int main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;++i)
    do_a_case(i+1);
    return 0;
}
