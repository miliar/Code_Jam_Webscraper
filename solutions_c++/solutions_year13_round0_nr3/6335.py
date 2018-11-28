

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>


using namespace std;


int reverse(int n)
{
    int m=0;
    while(n!=0){
        m=10*m+(n%10);
        n=n/10;
    }

    return m;
}

int main()
{
    ofstream out("a.out");
    ifstream in("a.in");

    int a,b,t,z,c=0;
    in>>t;
    for(int i=0;i<t;i++)
    {
        in>>a>>b;
        c=0;
        z=(int)sqrt((float)a);
        if(z*z<a) z++;
        while((z*z)<=b){
            if(reverse(z*z)==z*z&&z==reverse(z)){
               // cout<<z*z<<endl;
                c++;
            }
            z++;
        }
        out<<"Case #"<<i+1<<": "<<c<<endl;
        

    }
    
    out.close();
    in.close();
    return 0;
}