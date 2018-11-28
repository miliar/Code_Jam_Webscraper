#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
unsigned long long notPrime(unsigned long long num){
        for (unsigned long long factor=2; factor<20;factor++){
                if (num%factor==0){
                        return num/factor;
                }
        }
        return 0;

}
int main(){
        int T;
        int N;
        int J;
        cin>>T>>N>>J;
        cout<<"Case #1:"<<endl;
        //Reverse order
        bool config[N];
        unsigned long long res[9];
        unsigned long long value = pow(2,N)-1;
        unsigned long long end = pow(2,N-1);
        while ((J>0)&&(value>end)){
                unsigned long long temp = value;
                int idx=0;
                while(temp) {
                        config[idx] = temp & 1;
                        temp = temp >> 1;
                        idx++;
                }
                int base=2;
                unsigned long long num=0;
                unsigned long long factor;
                bool cont = true;
                do{
                        num=0;
                        for (int i=N-1;i>=0;i--){
                                num = num*base + config[i];
                        }
                        factor = notPrime(num);
                        if (factor == 0){
                                cont=false;
                        }
                        else{
                                res[base-2]=factor;
                        }
                        base++;
                }while((base<=10) && cont);
                if(cont){
                        J--;
                        for (int i=N-1;i>=0;i--){
                                cout<<config[i];
                        }
                        for (int i=0;i<9;i++){
                                cout<<" "<<res[i];
                        }
                        cout<<endl;

                }
                value -= 2;
        }
        return 0;

}
