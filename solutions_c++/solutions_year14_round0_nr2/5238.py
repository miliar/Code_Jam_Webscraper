#include <iostream>

using namespace std;

int main()
{
    int n;
    double C,F,X;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        double armTime=0.0000000;
        double cookies=2.0;
        cin>>C>>F>>X;
        double melhorOp = X/cookies;
        double t = C/cookies;
        cout<<"Case #"<<i+1<<": ";
        if(melhorOp<t)
        {
           std::cout.precision(7);
            std::cout << std::fixed <<melhorOp<<endl;
        }
        else{
        double vT = X/C;
        melhorOp = (C/cookies)*vT;
        armTime+=C/cookies;
        cookies+=F;
        while((((C/cookies)*vT)+armTime)<melhorOp)
        {

                melhorOp =((C/cookies)*vT)+armTime;
                armTime+=C/cookies;
                cookies+=F;


        }
            std::cout.precision(7);
            std::cout << std::fixed <<melhorOp<<endl;
}
    }
    return 0;
}
