#include <iostream>
#include <fstream>
#include <math.h>


using namespace std;

int main()
{   int cc=0; string st; int k=1; int c=1; int s=1;
    ifstream f("io.txt"); ofstream ff; ff.open("ot.txt");
    f>>cc; getline(f,st);

    for(int a=1; a<cc+1;a++){string str; k=1; c=1; s=1;
             f>>k; f>>c; f>>s; getline(f,str);
            // cout<<pow(k,c);
             //if (pow(k,c)<s) s=pow(k,c);
             ff<<"Case #"<<a<<": ";
             for(int i=1; i<s+1;i++){ff<<i<<" ";}
             ff<<endl;

    }
}
