#include<iostream>
#include<fstream>
#include<map>
using namespace std;
main(){
    ifstream in("B-large.in");
    ofstream out("output.txt");
    long long Test;
    in>>Test;

    for(int t=1;t<=Test;t++){
        string s;
        in>>s;
        long counter=0;
        long length = s.size();
        //out<<length;
        for(long i=0; i< length;i++){
            if(i == length-1 && s[i]=='-')
                counter++;
            if(i > 0 && s[i] == '-' && s[i-1] == '+')
                counter++;
            if(i > 0 && s[i] == '+' && s[i-1] == '-')
                counter++;

        }
        out<<"Case #"<<t<<": "<<counter<<endl;
    }
}

