#include <iostream>
#include <fstream>
using namespace std;

string m(string a){
    int i,ma;
    string b,c,d;
    ma = (int)a[0];
    for(i=1; i<a.length(); i++){
            if((int)a[i]>=ma){
                ma = (int)a[i];
                b+=a[i];
            }
            else{
                c+=a[i];
            }
    }
    for(i=b.length()-1; i>=0; i--) d+=b[i];
    d+=a[0];
    for(i=0; i<c.length(); i++) d+=c[i];
    return d;
}

int main() {
    ifstream fin;
    ofstream fout;
    fin.open("A-small-attempt0.in");
    fout.open("A-small-attempt0.out");
    int i,n;
    string a;
    cin>>n;
    for(i=0; i<n; i++){
        cin>>a;
        m(a);
        cout<<"Case #"<<i+1<<": "<<m(a)<<endl;
    }
    return 0;
}
