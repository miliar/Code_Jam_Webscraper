#include <iostream>
#include <fstream>
using namespace std;
bool l[10];



void split(int n)
{
    int t =0;
    while (n!=0)
    {
        t = n%10;
        if (!l[t])
        {
            l[t] = true;
        }
        n = n/10;
    }
}

int main()
{
    int n;
    int t;
    ofstream opf;
    ifstream ipf;
    ipf.open("A-small-attempt2.in");
    opf.open("output.txt");
    ipf >>t;
    for(int j=1;j<=t;j++)
    {

    ipf >> n;
    for(int i=0;i<=9;i++) l[i]=false;
    int n2 =n;
    bool tmp=true;
    int c =0;

    if (n==0) opf <<"Case #" << j<< ": INSOMNIA"<<endl;
    else{
        for(int i=0;i<=9;i++) if(l[i]) c++;
        while (c!=10)
        {
            c =0;
            split(n);
            n = n+n2;
            for(int i=0;i<=9;i++) if(l[i]) c++;
        }
        opf << "Case #" << j<< ": "<<n-n2<<endl;
    }

    }

}



