#include <iostream>
#include <fstream>

#define cin in
#define cout out

using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");

int main()
{
    int t;
    cin>>t;
    for (int i=0;i<t;i++)
    {
        double c,f,x;
        cin>>c>>f>>x;
        double pr=0;
        double mn=x*1./2;
        for (int j=1;j<100001;j++)
        {
            pr=pr+c*1./(f*(j-1)+2);
            mn = min(mn,pr+x*1./(f*j+2));
        }
        cout.precision(8);
        cout<< fixed<<"Case #"<<i+1<<": "<<mn<<endl;
    }
}