 #include <iostream>
#include<iomanip>
using namespace std;

int main() {
    // your code goes here
    int t;
    double c,f,x,min,r,w,f1;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        min=0;
        r=2;
        cin>>c>>f>>x;
        if(x<=c)
        {
            min=x/r;
            cout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<min<<endl;
        }
        else
        {
                w=x/r;
                    f1=c/r;
                while(1)
                {
                    r=r+f;
                    if(f1+x/r>w)
                    {
                        break;
                    }
                    min+=f1;
                    f1=c/r;
                    w=x/r;
                }
                min+=w;
                cout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<min<<endl;
           
        }
    }
    return 0;
}
