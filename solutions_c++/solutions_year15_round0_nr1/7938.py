#include <iostream>
#include <string>
#include <fstream>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("output.txt");

int num(char k)
{
    return k-'0';
}

int main()
{
    string s;
    int n, T;
    fin>>T;

    for(int kk=1;kk<=T;kk++){
        //cout<<kk<<endl;
        fin>>n;
        fin>>s;
        int ans = 0;
        int j = num(s[0]);
        int d;
        for(int i = 1; i<=n; i++){
            d = num(s[i]);
            //cout<<i<<" "<<d<<" ";
            if(d>0){
            if(i>j+ans){ans += i-j-ans;}
            j += d;
            }
        }
        fout<<"Case #"<<kk<<": "<<ans<<endl;
        //cout<<endl<<endl<<endl;
    }
}
