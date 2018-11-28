#include<iostream>
#include <fstream>    // To read in and write out files, and includes istream.getline(char* s, streamsize n, char delim).
#include <stdlib.h>   // Includes the "atoi" function.
#include <string>
using namespace std;
int main(){
    ifstream in ("A-large.in");         // The file we want to read in.
  ofstream out("A-large.out");
    int t;string line;
    //cin>>t;
    getline(in, line, '\n');            // |   then need to read in each line, and then have the great
  t = atoi(line.c_str());
    for(int j=1;j<=t;j++){
        int sm; char a[1002]; int n=0,c=0;
        in>>sm;
        in>>a;
        if(a[0]!='0'){
                n=n+a[0]-48;

        }
        else
        {c++;n++;}
//cout<<'0'-48;
        for(int i=1;i<=sm+1;i++){
                if(a[i]=='0')
                continue;
                if(n>=i)
                    n=n+a[i]-48;
                else
                {
                    c=c+(i-n);
                    n=i+a[i]-48;
                }


        }
        out<<"Case #"<<j<<": "<<c<<endl;
    //    t--;
    }

return 0;}
