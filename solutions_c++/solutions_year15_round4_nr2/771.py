#include <bits/stdc++.h>
using namespace std;


int main()
{
    ios_base::sync_with_stdio(false);
    ifstream in("input.txt");
    ofstream out("output.txt");
    #define cin in
    #define cout out
    int nb_cas;
    cin>>nb_cas;
    for(int cas=1;cas<=nb_cas;cas++)
    {
        cout<<"Case #"<<cas<<": ";
        int N;
        cin>>N;
        double V,X;
        cin>>V>>X;
        vector<double> R(N),C(N);
        for(int c=0;c<N;c++) cin>>R[c]>>C[c];

        if(N==1)
        {
            if(abs(C[0]-X) > 1e-8)
            {
                cout<<"IMPOSSIBLE"<<endl;
                continue;
            }
            double res = V/(R[0]);
            cout<<fixed<<setprecision(10)<<res<<endl;
            continue;
        }
        if((C[1] - X < -1e-8 && C[0] - X < -1e-8) ||  (C[1] - X > 1e-8 && C[0] - X > 1e-8))
        {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        if(abs(C[1]-C[0]) < 1e-8)
        {
            double res = V/(R[0]+R[1]);
            cout<<fixed<<setprecision(10)<<res<<endl;
            continue;
        }
        if(abs(C[1]-X) < 1e-8)
        {
            double res = V/R[1];
            cout<<fixed<<setprecision(10)<<res<<endl;
            continue;
        }
        if(abs(C[0]-X) < 1e-8)
        {
            double res = V/R[0];
            cout<<fixed<<setprecision(10)<<res<<endl;
            continue;
        }
        double V1 = V*(X-C[0])/(C[1]-C[0]);
        double V0 = V - V1;
        if(min(V1,V0) < 0)
        {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        else
        {
            double res = max(V0/R[0],V1/R[1]);
           cout<<fixed<<setprecision(10)<<res<<endl;
        }
    }
}
