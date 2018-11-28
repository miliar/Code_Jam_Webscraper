#include <iostream>
#include <fstream>
using namespace std;

int main () {
    ifstream fi;
    ofstream fo;
    //fi.open ("tinput.txt");    fo.open ("toutput.txt");

    //fi.open ("B-small-attempt2.in"); fo.open ("q2_output.txt");
    fi.open ("B-large.in");          fo.open ("q2_output_large.txt");

    int t,i=0, j=0,n,k;


    char ch;
    fi>>t;                                  //cout<<t<<"\n";
  //  fi>>ch;
    while(++j<= t){                          cout<<"\nCase #"<<j<<": ";
       fi>>n;
       int h[2501] = {};                              //cout<<" "<<n;
       int r = 2*(n*n) - n;
       for(i = 1; i<=r; ++i){
            fi>>k;                            // cout<<" "<<k;
            if(h[k] == 0) h[k]=1;
            else          h[k]=0;
       }
       fo<<"Case #"<<j<<": ";

       for(i=1;i<=2500;++i){
            if(h[i] == 1) {
                fo<<i<<" ";                       cout<<i<<" ";
            }
       }
       fo<<"\n";                                   // cout<<endl;

    }//end of one test case

    fi.close();
    fo.close();
    return 0;
}
