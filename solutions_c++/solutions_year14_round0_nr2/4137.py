#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
    cout.precision(8);
    fstream f1,f2;
    int t;
    f1.open("CJcookieclikerf",ios::in);
    f2.open("output",ios::out);
    f1.seekg(0);
    f1>>t;
    for(int i=0;i<t;i++)
    {
        f2<<"Case #"<<i+1<<": ";
        double initiate=2,C,F,X,totalt=0,temp1,temp2;
        f1>>C>>F>>X;
        while(1)
        {
            temp1=(C/initiate)+(X/(initiate+F));
            temp2=X/initiate;
            if(temp1>temp2)break;
            else
            {
                totalt+=(C/initiate);
                initiate+=F;
            }
        }
        totalt+=(X/initiate);
        f2<<std::fixed<<setprecision(7)<<showpoint<<totalt<<endl;
    }
    return 0;
}
