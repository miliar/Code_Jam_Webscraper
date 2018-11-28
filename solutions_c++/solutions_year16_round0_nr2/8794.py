#include <iostream>
#include <fstream>
using namespace std;

int main () {
    ifstream fi;
    ofstream fo;
    //fi.open ("tinput.txt");
    //fo.open ("toutput.txt");

    //fi.open ("B-small-attempt1.in");B-large
    fi.open ("B-large.in");
    fo.open ("q2_large_output.txt");

    int t,i=0,count=0, j;
    char cn, co, s[101];
    fi>>t;                      //cout<<t<<"\n";
    fi.getline(s,101);
    while(++i<= t){
        j = 2;
        count = 0;
        fi.getline(s,101);

        co = s[0];              //cout<<i<<":"<<co<<" ";

        cn = s[1];              //cout<<cn<<" ";
        while(cn != '\0'){
            if(co != cn) count++;
            co = cn;
            cn = s[j++];
        }
        if(co == '-') count++;

        fo<<"Case #"<<i<<": "<<count<<endl;        //cout<<count<<endl;
    }

    fi.close();
    fo.close();
    return 0;
}
