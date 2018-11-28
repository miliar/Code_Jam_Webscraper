#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream que;
    ofstream ans;
    //que.open("C:\\Users\\Kushagra\\Downloads\\input.txt");
    que.open("C:\\Users\\Kushagra\\Downloads\\B-large.in");
    ans.open("C:\\Users\\Kushagra\\Downloads\\output2.txt");

    int T;
    double C,F,X;
    int i=0;

    que>>T;
    ans.precision(7);
    ans.setf(ios::fixed,ios::floatfield);
    while(T--)
    {
        que>>C>>F>>X;
        double mini=X/2.0;
        double Xdenom=2.0+F;
        double Ydenom=2.0;
        double prod=0.0;
        while(mini>prod+X/Xdenom)
        {
            prod+=C/Ydenom;
            mini=min(mini,prod+X/Xdenom);
            Xdenom+=F;
            Ydenom+=F;
        }
        ans<<"Case #"<<++i<<": "<<mini<<"\n";
    }
    return 0;
}
