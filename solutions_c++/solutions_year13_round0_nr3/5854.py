#include<iostream>
#include<fstream>
#include <sstream>
#include <math.h>

using namespace std;

typedef unsigned long long int cunto;
cunto pw(cunto x){
    return x*x;
}
bool pl(long int x){

    string text;          // string which will contain the result
    ostringstream convert;   // stream used for the conversion
    convert << x;      // insert the textual representation of 'Number' in the characters in the stream
    text = convert.str();
    cunto l = text.length();
    for ( cunto i = 0; i < l/2;i++){

        if (text[i] != text[l-i-1] ){
            return false;
        }
    }
    return true;
}

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");
	int N;
	in>>N;
    for ( int n = 0; n < N; n++){
        cunto A,B;
        in>>A>>B;
        cunto ctr = 0;
        cunto i = ceil(sqrt(A));
        cunto result = pw(i);
        while (result<=B){
            if (pl(result) && pl(i)){
                ctr++;
                cout<<i<<' '<<result<<endl;
            }
            result = pw(++i);
        }
        out<<"Case #"<<n+1<<": "<<ctr<<endl;
    }
}
