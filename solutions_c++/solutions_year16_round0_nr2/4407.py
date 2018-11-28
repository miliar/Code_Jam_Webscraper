#include <fstream>
#include <cmath>
#include <string>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int solve(const string& a) {
    int i,k=0;
    for(i=1; i<a.length(); ++i) {
        if(a[i] != a[i-1])
            ++k;
    }
    if(a[0]=='+' && k%2==1)
        ++k;
    else if(a[0]=='-' && k%2==0)
    ++k;
    return k;
}

int main()
{
    int n,m;
    string s;
    fin>>n;
    for(int i=0; i<n; ++i) {
        fin >> s;
        m = solve(s);
        fout << "Case #" << i+1 << ": " << m << endl;
    }
    return 0;
}

