#include<iostream>
#include<fstream>
using namespace std;

main (){
    ifstream inn;
    inn.open("B-large.in");
    ofstream out;
    out.open("out.txt");
    long long casenum;
    inn>>casenum;

    long long c=0;
    string str="";
    for(long i=1;i<=casenum;i++){

        inn>>str;
        c=0;
        for (long long j=0;j<str.length();j++)
        {

            if (str[j]=='-' and (j+1)==str.length())
            {
                c++;
            }else if (str[j]!=str[j+1] and (j+1)!=str.length()){
                c++;
            }

        }
        out<<"Case #"<<i<<": "<<c<<endl;
    }
}
