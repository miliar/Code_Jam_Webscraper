#include<iostream>
#include<fstream>
#include<map>
using namespace std;
main(){
    ifstream in("B-small-attempt0.in");
    ofstream out("output.txt");
    long long Test;
    in>>Test;

    for(int t=1;t<=Test;t++){
        string s;
        in>>s;
        long counter=0;
        for(int i=s.size()-1;i>=0;i--){
            if(s[i]!=s[i-1])
                counter++;

        }
        if(s[s.size()-1]=='-')
            counter++;
        out<<"Case #"<<t<<": "<<counter-1<<endl;
    }
}

