#include<string>
#include<fstream>
#include<sstream>
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
int mintimes(string a1, char tar){
    int n = a1.size();
    if (n==1) {
        if (a1[0]==tar) {
            return 0;
        }
        else
            return 1;
    }
    if (a1[n-1]==tar)
        return mintimes(a1.substr(0, (n-1)), tar);
    else{
        if (tar=='+') {
            tar='-';
        }
        else
            tar = '+';
        return mintimes(a1.substr(0, (n-1)), tar)+1;
    }
}
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
    string a2;
    getline(matches, r);
    n-=1;
    for (int i = 0; i<n; i++){
        vector<int> res(10, 0);
        getline(matches, r);
        istringstream r1(r);
        char tar = '+';
        r1>>a1;
        int times = mintimes(a1, tar);
        output<<"Case #"<<i+1<<": "<<times<<endl;
    }
    return 0;
}
