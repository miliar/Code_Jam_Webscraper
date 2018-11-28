#include <fstream>
using namespace std;

int main()
{
    int t;
    int k,c,s;
    ofstream opf;
    ifstream ipf;
    ipf.open("D-small-attempt0.in");
    opf.open("output.txt");
    ipf >>t;
    for(int j=1;j<=t;j++)
    {
        ipf >> k >> c >>s;
        opf << "Case #" <<j<< ": ";
        for(int i=1;i<=k;i++) opf << i<< " ";
        opf << endl;
    }
}
