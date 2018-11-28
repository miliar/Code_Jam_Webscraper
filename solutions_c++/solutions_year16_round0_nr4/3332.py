#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream in("C:\\Users\\Abhi\\Downloads\\D-small-attempt0.in");
    ofstream out("C:\\Users\\Abhi\\Downloads\\D-small-attempt0.out");
    int t,k,c,s;
    in>>t;
    int i;
    for(i=0;i<t;++i){
        in>>k>>c>>s;
        out<<"Case #"<<i+1<<": ";
        int j;
        for(j=1;j<=k;++j)
            out<<j<<' ';
        out<<endl;
    }
}
