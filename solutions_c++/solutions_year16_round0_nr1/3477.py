#include <iostream>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

set<int> get_digits(long long N){
    set<int> digits;
    while(N){
        digits.insert(N%10);
        N /= 10;
    }

    return digits;
}

int main(){

    int T;
    ifstream din;
    ofstream dout;

    din.open("A-large.in", ifstream::in);
    dout.open("A-large.out", ofstream::out);

    din>>T;

    for(int t=0; t<T; t++){
        long long N;
        din>>N;
        if(N == 0){
            dout<<"Case #"<<(t+1)<<": INSOMNIA"<<endl;
            continue;
        }
        int counts[10];
        int unseen = 10;
        for(int i=0; i<10; i++)
            counts[i] = 0;

        int i=1;
        while(unseen != 0){
            set<int> digits = get_digits(i*N);
            for(set<int>::iterator it=digits.begin(); it!=digits.end(); ++it){
                if(counts[*it] == 0)
                    unseen--;
                counts[*it]++;
            }
            i++;
        }
        dout<<"Case #"<<(t+1)<<": "<<(i-1)*N<<endl;
    }
    din.close();
    dout.close();
    return 0;
}
