#include<string>
#include<fstream>
#include<sstream>
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;

int main(int argc , char ** argv){
    ifstream match(argv[1]);      //open a file
    ofstream output(argv[2]);     //write into a file
    int n=0;
    string line ;
    while( getline(match, line) ){
        ++n;
    }
    ifstream matches(argv[1]);
    string r;
    string a1;
    getline(matches, r);
    n-=1;
    for (int i = 0; i<n; i++){
        getline(matches, r);
        istringstream r1(r);
        r1>>a1;
        string a2;
        char aa = a1[0];
        a2+=aa;
        for (int i = 1; i<a1.size(); i++) {
            if (a1[i]<aa) {
                a2+=a1[i];
            }
            else{
                a2=a1[i]+a2;
                aa=a1[i];
            }
        }
        output<<"Case #"<<i+1<<": "<<a2<<endl;
    }
    return 0;
}
