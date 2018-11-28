#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

vector<bool> v(10,false);

bool elemez(int a)
{
    while(a!=0)
    {
        v[a%10]=true;
        a/=10;
    }
    for(int i=0; i<10; ++i) if(!v[i]) return false;
    return true;
}

int main()
{
    ifstream f;
    string fname="2.txt";
    f.open(fname.c_str());
    int n;
    f>>n;
    for(int k=0; k<n; ++k)
    {
        v.assign(10,false);
        int a;
        f>>a;
        if(a==0) cout<<"Case #"<<k+1<<": INSOMNIA"<<endl;

        else
        {
            int d=a;
        while(true)
        {
            if(elemez(a))
            {
                cout<<"Case #"<<k+1<<": "<<a<<endl;
                break;
            }
            else{a+=d;}
        }
        }


    }


    return 0;
}
