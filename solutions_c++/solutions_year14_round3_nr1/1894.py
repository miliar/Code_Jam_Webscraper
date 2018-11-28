#include <iostream>
#include <fstream>
#include <math.h>


using namespace std;


int gcd(int a, int b)
{
    int c;
    if (a>b){int s=a; a=b; b=s;}
    while ( a != 0 ) {
        c = a; a = b%a;  b = c;
    }
    return b;
}

int main()
{
    ifstream f("A-small-attempt1.in");
    ofstream fki("out.txt");
    long long teszt=pow(2,40);
    cout<<teszt<<endl;
    long long int sz,n;
    char c;
    int t;
    f>>t;
    //t=1;
    for (int i=1; i<=t; i++)
    {
        f>>sz>>c>>n;//szamlalo, nevezo
        //cout<<sz<<"/"<<n<<endl;
        long long int gc=gcd(sz,n);
        sz/=gc;
        n/=gc;
        int tag=0;
        for (int k=1; k<=40 && sz>0; k++)
        {
            if (sz*pow(2,k)>=n)
            {   if (tag==0){tag=k;cout<<tag<<endl;}
                long long int g=gcd(pow(2,k),n);
                long long int m1=pow(2,k)/g;
                sz*=m1;
                n=n*pow(2,k)/g;
                sz-=n/g;
                //cout<<m1<<" "<<sz<<"/"<<n<<endl;
            }
        }
        fki<<"Case #"<<i<<": ";
        if (sz==0){fki<<tag;}else{fki<<"impossible";}
        fki<<endl;
    }
    cout << "Hello world!" << endl;
    return 0;
}
