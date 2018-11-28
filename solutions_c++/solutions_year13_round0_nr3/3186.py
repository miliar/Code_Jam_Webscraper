// normal_distribution
#include <iostream>
#include <random>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <sstream>
#include <string>
#include <cmath>
using namespace std;


bool ispar(string str){
    int len=str.length();
    for(int n=0;n<len/2;n++){
        if(str[n]!=str[len-n-1])
            return false;
    }
    return true;
}

bool ispar(__int64 n){
    stringstream ss;
    ss<<n;
    string str;
    str=ss.str();
    return ispar(str);
}

int main(){
    ifstream in("input.txt");
    ofstream cout("output.txt");
    //istream& in=cin;

//    int s;
//    while(cin>>s)
//        cout<<ispar(s);

    int T;
    __int64 N,M;
    in>>T;
    for(int t=0;t<T;t++){
        in>>N>>M;
//        cout<<N<<endl;
//        cout<<M<<endl;
        int cnt=0;
        for(int n=N;n<=M;n++){
            //check each one
            if(!ispar(n))  continue;
            // check if it is a square of a par
            int sr = int(sqrt(n));
//            if(n==121){
//                cout<<"121"<<endl;
//            }
            if(ispar(sr)) {
                //cout<<pow(sr,2)<<" "<<n<<endl;
                double tmp=pow(double(sr),2);
                if(int(tmp)==n){
                    cnt++;
                    //cout<<n<<endl;
                }
            }

        }

        cout<<"Case #"<<t+1<<": "<<cnt<<endl;
    }
//        for(int i=0;i<N;i++){
//            for(int j=0;j<M;j++)
//                cout<<mat(i,j);
//            cout<<endl;
//        }

    return 0;
}
