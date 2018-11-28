#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(int argv, char** argc)
{
    fstream fin, fout;
    fin.open(argc[1], ios::in);
    fout.open(argc[2],ios::out);
    int numCase;
    fin>>numCase;
    string strin, strout;
    char temp;
    for( int i=0; i<numCase; ++i){
        fin>>strin;
        strout = strin;
        for( int j=1; j<strout.length(); ++j ) {
            if( strout[j] >= strout[0] ) {
                temp = strout[j];
                for( int k=j; k>=1; --k ){
                    strout[k] = strout[k-1];
                }
                strout[0] = temp;
            }
        }
        fout<<"Case #"<<i+1<<": "<<strout<<endl;
    }
    fin.close();
    fout.close();
}

