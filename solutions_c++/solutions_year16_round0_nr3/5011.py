#include <iostream>
#include <bitset>
#include <set>
#include <fstream>
#include <string>
#include <stdio.h>      /* printf, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <math.h>       /* time */

using namespace std;

bool mask_bit(char*,int);

int main(int argc,char *argv[]){

    fstream fs(argv[1],fstream::in);
    const long size=1024*64;
    long is_prime[size +1] = {0};
    is_prime[0] = 1;
    is_prime[1] = 1;
    for(long i=2; i<=size; i++){
        if(is_prime[i] == 0){
            for(long mul = 2; (i*mul) <=(size);mul++){
                is_prime[i*mul] = 1;
            }
        }
    }
    int NUM;
    fs >> NUM;

    for(int in_index=0; in_index<NUM; in_index++){
        cout<<"Case #"<<in_index+1<<":"<<endl;
        int N,J;
        fs >> N >> J;
        long high_mask = 1 << (N-1);
        long low_mask  = 1;
        int mod_num = 1 << (N-2);
        set<long> select_num;
        set<long>::iterator it;
        while( J > 0){
            long rand_num = rand() % mod_num;
            while(  select_num.find(rand_num) !=  select_num.end() ){
                rand_num = rand() % mod_num;
            }
            select_num.insert(rand_num);
            
            long test_num = high_mask | ((rand_num)<<1) | low_mask;
            bool check_valid=true;
            long base_val[11];
            int base;
            for(base=2; base<=10; base++){
                long num_new_base =0;
                long cpy_num = test_num;
                long mul = 0;
                // num_new_base is value under new test
                while(cpy_num != 0){
                    //cout << "base: "<<base<<" mul: "<<mul<<endl;
                   long exp_num = pow(base,mul);
                   num_new_base += ((cpy_num & 0x1) * exp_num);
                   cpy_num = cpy_num >> 1;
                   mul++;
                }
                //cout<<"end loop"<<endl;
                //base_val[base] = num_new_base; 
                //cout<<"end3 loop"<<endl;
                // test this number whether prime
                bool check_prime=true;
                //cout<<"end4 loop"<<endl;
                
                for(long i=2; i<=size; i++){
                    if(i >= num_new_base){
                        break;
                    }
                    //cout<<"end5 loop"<<endl;
                    if(is_prime[i] == 0){
                        //cout<<"end6 loop"<<endl;
                        if( (num_new_base % i) == 0){
                            //cout<< "num_div "<<num_new_base<<" "<<i<<endl;
                            check_prime = false;
                            base_val[base] = i;
                            break;
                        }
                    }
                    //cout<<"i "<<i<<endl;
                }
                //cout <<"end2 loop\n";
                if( check_prime == true){
                    check_valid = false;
                    break;
                }
            }
            if(check_valid == true){
                string s = bitset< 64 >( test_num ).to_string();
                s.erase(0,s.length()-N);
                //cout << bitset<32>(test_num);
                cout << s;
                for(int i=2; i<=10; i++){
                    cout << " " << dec<< base_val[i];
                }
                cout << endl;
                J--;
            }

        }

    }


    fs.close();
    return 0;
}

