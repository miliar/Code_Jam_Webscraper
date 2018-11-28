#include <iostream>
#include<stdio.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    int q=t;
    while(t--)
    {
        double c,f,x,cr,tt=0,lt,nr;
        cin>>c>>f>>x;
        cr=2.0;
        //lt=c/2;
        nr=c/2;
        while(x/cr>(c/cr+x/(cr+f)))
              {
                  tt+=c/cr;
                    cr+=f;
              }
                tt+=x/cr;
                //cout<<tt<<"\n";
                cout<<"Case #"<<q-t<<": ";
                printf("%.7lf\n",tt);
    }
    //cout << "Hello world!" << endl;
    return 0;
}
