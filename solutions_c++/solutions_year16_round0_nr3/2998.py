#include <iostream>
#include <stdlib.h>
#include <vector>
#include <fstream>
#include <time.h>
#include <cmath>
using namespace std;

long get_divisor(long num){

    long N = sqrt(num);
    for(long n=2; n<N; n++){
        if(num%n ==0 )
            return n;
    }
    return 0;
}

long bits2num(string bits, long r){
    long ans = 0;
    int N = bits.length();
    for(int i=0; i<N; i++){
        if(bits[i] == '1')
            ans += pow(r, N-1-i);
    }
    return ans;
}

bool isPresent(string bits, vector<string> Bits){
    for(vector<string>::iterator it=Bits.begin(); it<Bits.end(); it++)
        if(*it == bits)
            return true;
    return false;
}

int main(){

    ofstream dout;
    dout.open("test.out", ofstream::out);

    srand(time(NULL));
    int N = 16;
    int J = 50;
    dout<<"Case #1:"<<endl;
    int j=0;
    vector<string> Bits;
    while(j<J){
        //cout<<j<<endl;
        string bits = "1";
        for(int n=0; n<N-2; n++){
            int r = rand()%100;
            if(r>50)
                bits += "1";
            else
                bits += "0";
        }
        bits += "1";
        if(isPresent(bits, Bits))
            continue;
        //cout<<bits;
        bool all_clear = true;
        vector<long> divisors;
        for(long r=2; r<=10; r++){
            long num = bits2num(bits, r);
            //cout<<" "<<num<<"_"<<r;
            long d = get_divisor(num);
            if(d==0){
                all_clear = false;
                break;
            }
            divisors.push_back(d);
        }
        //cout<<endl;
        if(all_clear){
            j++;
            dout<<bits;
            Bits.push_back(bits);
            for(vector<long>::iterator it= divisors.begin(); it!=divisors.end(); ++it)
                dout<<" "<<(*it);
            dout<<endl;
        }

    }
    dout.close();
    return 0;
}
