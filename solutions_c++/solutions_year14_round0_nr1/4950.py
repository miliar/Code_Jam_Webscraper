#include <iostream>
#include <algorithm>
using namespace std;

#include <fstream>
using std::ifstream;
using std::ofstream;

int value;


int main(){
    
    ifstream indata;
    ofstream outdata;
    int t;
    indata.open("A-small-attempt0.in");
    outdata.open("A-small-attempt0.txt");
    indata>>t;
    for(int i=1; i<=t; i++){        
        int r1;
        int a[4], b[4];
        indata>>r1;
        --r1;
        for(int j=0; j<4; j++){
            if(j==r1){    
                for(int k=0; k<4; k++){
                    indata>>a[k];
//                    outdata<<a[k]<<" ";
                }
//                outdata<<"\n";
            }
            else{    
                for(int k=0; k<4; k++){
                    int c;
                    indata>>c;
                }
            }
        }
        int r2;
        indata>>r2;
        --r2;
        for(int j=0; j<4; j++){
            if(j==r2){    
                for(int k=0; k<4; k++){
                    indata>>b[k];
//                    outdata<<b[k]<<" ";
                }
//                outdata<<"\n";
            }
            else{    
                for(int k=0; k<4; k++){
                    int c;
                    indata>>c;
                }
            }
        }
        sort(a, a+4);
        sort(b, b+4);
/*        for(int k=0; k<4; k++){
            outdata<<a[k]<<" ";
        }
        outdata<<"\n";
        for(int k=0; k<4; k++){
            outdata<<b[k]<<" ";
        }
        outdata<<"\n"; */
        int count=0;
        int value;
        int j=0, k=0;
        while(j<4 && k<4){
            if(a[j]<b[k])
                ++j;
            else if(a[j]>b[k])
                ++k;
            else{
                ++count;
                value=a[j];
                ++j; ++k;
            }
        }
//        outdata<<count<<"\n";
        if(count==1)
            outdata<<"Case #"<<i<<": "<<value<<"\n";
        else if(count>1)
            outdata<<"Case #"<<i<<": Bad magician!\n";
        else if(count==0)
            outdata<<"Case #"<<i<<": Volunteer cheated!\n"; 
    }
    indata.close();
    outdata.close(); 
    
}
