#include <iostream>
#include <fstream>
using namespace std;

int pow(unsigned long long n, unsigned long long p){
    unsigned long long k=1;
    for(unsigned long long i=0;i<p;i++){
        k*=n;
    }
    return k;
}


int main(){
    ifstream input("input.txt");
    ofstream output("output.txt");
    unsigned long long n;
    input >> n;
    unsigned long long var_n;
    unsigned long long digit[10];
    unsigned long long alldigits;
    unsigned long long k, num;
    for(unsigned long long i=0;i<n;i++){
        alldigits=10;
        for(unsigned long long j=0;j<10;j++){
            digit[j]=0;
        }
        input >> var_n;
        output << "Case #" << i+1 << ": ";
        if(var_n==0){
            output << "INSOMNIA" << endl;
        }

        else{
            k=0;

            while(alldigits>0){
                k++;
                num=k*var_n;
                unsigned long long num_cifre=1;

                while(true){
                    if(num/pow(10,num_cifre-1)>=10)
                        num_cifre++;
                    else
                        break;
                }
                //cout << num << " → ";
                while(num_cifre>0){
                    unsigned long long da_valutare=num/pow(10,num_cifre-1);
                    //cout << da_valutare << " ";
                    if (digit[da_valutare]==0){
                        digit[da_valutare]=1;
                        alldigits--;
                    }
                    num=num-num/pow(10,num_cifre-1)*pow(10,num_cifre-1);
                    num_cifre--;
                }
                //cout << endl;

            }
            output << k*var_n << endl;
        }

    }
    return 0;

}
