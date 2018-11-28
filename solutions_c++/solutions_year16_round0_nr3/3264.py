#include <iostream>
#include <fstream>
#include <bitset>
#include <cmath>
using namespace std;

int getDivisor(long long int n){
    for(long long int i=2;i*i<=n;i++){
        if(n % i == 0) return i;
    }
    return -1; //prime
}
int main(){
    ifstream input("C-small-attempt1.in");
    ofstream output("smallC.txt");
    int t, n, j;
    input >> t; //t will always be 1 though

    input >> n >> j;

    int total = 0;
    cout << "Case #1:\n";
    output << "Case #1:\n";

    for(int i=pow(2, n-1)+1;i<pow(2, n);i+=2){
        bitset<16> bits(i);
        long long int divs[9] = {};
        bool done = true;

        string str = bits.to_string<char,std::string::traits_type,std::string::allocator_type>();
        for(int k=2;k<=10;k++){
            long long int num = strtoll(str.c_str(), NULL, k);
            //cout << str << " " << k << " ";
            //cout << num << endl;
            long long int div = getDivisor(num);
            if(div == -1){
                done = false;
                break;
            }
            else divs[k-2] = div;
        }
        if(done){
            cout << str << " ";
            output << str << " ";
            for(int k=0;k<9;k++){
                cout << divs[k] << " ";
                output << divs[k] << " ";
            }
            cout << endl;
            output << endl;
            total++;
            if(total >= j) break;
        }
    }
	input.close();
	output.close();
	return 0;
}
