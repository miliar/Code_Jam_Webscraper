#include <fstream>
#include <cmath>
#include <string>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

const long long MAX_N = 100000; 
bool v[10];

void add(long long m) {
    while(m) {
        v[m%10] = 1;
        m/=10;
    }
}

bool check(){
    for(int i=0; i<10; ++i)
        if(!v[i])
            return false;
    return true;
}

long long solve(long long a) {
    if(a == 0)
        return -1;
    int i;
    
    for(i=0; i<10; ++i)
        v[i] = 0;
    long long n;
    long long m;
    for(n=1; n<MAX_N;++n) {
        m = n*a;
        add(m);
        if(check())
            return m;
    }
    return -1;
}

int main()
{
    int n;
    long long a,m;
    fin>>n;
    for(int i=0; i<n; ++i) {
        fin >> a;
        m = solve(a);
        fout << "Case #" << i+1 << ": " ;
        if(m == -1)
            fout << "INSOMNIA";
        else
            fout << m;
        fout << endl;
    }
    return 0;
}

