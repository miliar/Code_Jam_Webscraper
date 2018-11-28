#include <iostream>
#include <fstream>
using namespace std;

int main () {
    ifstream fi;
    ofstream fo;
    //fi.open ("tinput.txt");    fo.open ("toutput.txt");

    //fi.open ("B-small-attempt1.in");B-large
    fi.open ("A-large.in");    fo.open ("q1_output_large.txt");

    int t,i=0, j=0,c1, c2, c;

    char ch, s[1001],bs[1001], l[1001];
    s[0] = 0;
    bs[0] = 0;
    fi>>t;                                  //cout<<t<<"\n";
    fi.getline(l,101);
    while(++j<= t){                          cout<<"Case #"<<j<<": ";
       c1=0; c2=0; c=0;
       fi.getline(l,1001);
       ch=l[c++];
       s[0] = ch;
       bs[0] = ch;
       while(ch != '\0'){

           ch = l[c++];                      //cout<<ch;
           if(ch >= bs[c2]) {
                bs[++c2] = ch;
           }
           else {
                s[++c1] = ch;
           }
       }
       fo<<"Case #"<<j<<": ";
       for(i=c2;i>0;--i){
            fo<<bs[i];                          cout<<bs[i];
       }
       for(i=0;i<c1;++i){
            fo<<s[i];
       }                                          cout<<s<<endl;
       fo<<"\n";                                   // cout<<endl;

    }//end of one test case

    fi.close();
    fo.close();
    return 0;
}
