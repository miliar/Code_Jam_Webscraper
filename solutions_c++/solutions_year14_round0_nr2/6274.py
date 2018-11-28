#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[])    {
    int cases; cin>>cases;

    double c,f,x;
    for(int i=1;i<=cases;i++)  {

        cin>>c>>f>>x;
        double cur = 2;
        double ret = 0;
        while(true) {
            if(x/cur<c/cur+x/(cur+f))   {
                ret += x/cur;
                break;
            }else   {
                ret += c/cur;
                cur = cur+f;
            }
        }
        cout<<fixed<<setprecision(7);
        cout<<"Case #"<<i<<": ";
        cout<<ret<<endl;
    }
    return 0;
}