#include<bits/stdc++.h>
#include<fstream>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;
void countdig(long n,long a[10]) {
    stringstream convert;
    convert << n;
    string s = convert.str();
    for(long i=0;i<s.length();i++) {
        a[s[i]-'0']++;
    }
}
long finish(long *a) {
    for(long i=0;i<10;i++) {
        if(a[i]==0) return 0L;
    }
    return 1L;
}
int main() {
    ofstream outfile;
    ifstream infile;
    infile.open ("C:\\Users\\vikram\\Documents\\c++\\code jam\\A-large.in");
    outfile.open ("C:\\Users\\vikram\\Documents\\c++\\code jam\\out.txt");
    long t;
    infile >> t;
    for(long i=1;i<=t;i++) {
        long dig[10],n;
        memset(dig,0,sizeof(dig));
        infile >> n;
        long np=n;
        while(finish(dig)!=1L && n!=0) {
            countdig(n,dig);
            n+=np;
        }
        if(n==0 || finish(dig)!=1) outfile << "Case #" <<i<<": INSOMNIA" << "\n";
        else outfile << "Case #"<<i<<": "<<n-np << "\n";
    }
    infile.close();
    outfile.close();
    return 0;
}
