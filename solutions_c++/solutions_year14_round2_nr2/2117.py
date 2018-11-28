#include<fstream>
#include<iomanip>
#include<iostream>

using namespace std;

int main(int argc, char**argv)
{
 ifstream in;
 ofstream out;
 unsigned int a,b,c;
 in.open("in");
 out.open("out");
 int ncases;
 in >> ncases;
 bool end = false;
 int ret;
 for(int i = 0; i < ncases; i++){
    ret = 0;
    in >> a;
    in >> b;
    in >> c;
    for(unsigned int j = 0; j < a; j++){
        for( int k = 0; k < b; k++){
            if((j & k) < c)
                ret++;
        }
    }
    cout << "Case #" << i + 1<< ": " << ret << endl;
 }
}


