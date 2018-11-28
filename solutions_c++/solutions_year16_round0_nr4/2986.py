#include <iostream>
#include <fstream>

using namespace std;

int k,c,s;

int main()
{
    int t;
    ifstream in("in.txt");
    ofstream out("out.txt");
    cin>>t;
    for(int p=1;p<=t;p++)
    {
    cin>>k>>c>>s;
        out<<"Case #"<<p<<": ";
        for(int i=1;i<=s;i++)out<<i<<" ";out<<endl;
    }
    return 0;
}
