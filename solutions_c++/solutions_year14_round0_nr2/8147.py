#include<iostream>
#include<iomanip>
using namespace std;

int main()
{


int t;
double c,f,x;
cin>>t;
int p=1;
while(p<=t)
{

    cin>>c>>f>>x;
    c=c/1;
    f=f/1;
    x=x/1;
    double r=2;
    double up=0;
    double down=0;
    double parent=0;
    while(up>=down)
    {
        up=parent+x/r;
        parent=parent+c/r;
        r=r+f;
        down=parent+x/r;
    }

cout<<"Case #"<<p<<": "<<fixed<<setprecision(7)<<up<<endl;

p++;

}





return 0;
}
