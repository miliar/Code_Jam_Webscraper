#include <iostream>
#include <fstream>

using namespace std;

int main(){
    string ff;
    cin >> ff;
    ifstream input;
    input.open(ff);
    ofstream output;
    output.open("c++/code_jam/sheep.txt");
    int T;
    input >> T;

    for (int i=0; i<T; ++i){
        long long N;
        input >> N;
        long long n=N;
        output << "Case #" << i+1 << ": ";
        if (n==0){
            output << "INSOMNIA\n";
            continue;
        }
        int t[10]={};
        int h=10;
        while (1){
            long long m=n;
            while (m>0){

                int c=m%10;
                m/=10;
                if (t[c]==0) --h;
                t[c]=1;
            }
            if (h==0){
                output << n << "\n";
                break;
            }
            n=n+N;
        }
    }

}
