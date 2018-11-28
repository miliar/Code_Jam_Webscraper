#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;

ifstream in;
ofstream out;
int main()
{
    string v;
    int sol[101];
    in.open("example.in");
    out.open("example.out");
    int n=0;
    int m;
    in>>m;
    char c;
    getline(in,v);
    for(int i=0;i<m;i++)
    {
        getline(in,v);
        n=v.length();
        if(v[0] == '-'){
            sol[0] = 1;
        } else {
            sol[0] = 0;
        }
        for(int i=1;i<n;i++){
            if(v[i] == '-'){
                if(v[i-1] == '-')
                    sol[i] = sol[i-1];
                else
                    sol[i] = sol[i-1] + 2;
            } else {
                sol[i] = sol[i-1];
            }
        }
        out <<"Case #" << i+1 << ": "<< sol[n-1] << "\n";
    }
    return 0;
}
