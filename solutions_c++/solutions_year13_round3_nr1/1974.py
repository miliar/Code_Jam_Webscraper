#include <string>
#include <iostream>
using namespace std;

bool isConsSq( const string &s, int i, int n ){
    while (n--) {
        if( s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u' ){
            return false;
        }
        i++;
    }
    return true;
}

int main() {
    int n,T,total,t,i,last;
    string s;
    
    cin>>T; T++;
    for( t=1; t<T; t++ ) {
        cin>>s>>n;
        total = 0;
        last = -1;
        
        for (i=0; i+n-1<s.size(); i++ ) {
            if( isConsSq(s,i,n) ){
                total+=( (i-last)*(1+s.size()-n-i) );
                last = i;
            }
        }
        cout<<"Case #"<<t<<": "<<total<<endl;
    }
    return 0;
}
