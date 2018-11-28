#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <stdint.h>

///////////////////////////////////////////////////////////////////////////////
/// http://stackoverflow.com/questions/4424374/determining-if-a-number-is-prime
//////////////////////////////////////////////////////////////////////////////////

uint64_t power(uint64_t a, uint64_t n, uint64_t mod)
{
 uint64_t power=a,result=1;

 while(n)
 {
  if(n&1)
   result=(result*power)%mod;
  power=(power*power)%mod;
  n>>=1;
 }
 return result;
}

uint64_t witness(uint64_t a, uint64_t n)
{
 uint64_t t,u,i;
 uint64_t prev,curr;

 u=n/2;
 t=1;
 while(!(u&1))
 {
  u/=2;
  ++t;
 }

 prev=power(a,u,n);
 for(i=1;i<=t;++i)
 {
  curr=(prev*prev)%n;
  if((curr==1)&&(prev!=1)&&(prev!=n-1))
   return true;
  prev=curr;
 }
 if(curr!=1)
  return true;
 return false;
}


//return a divisor - 0 if prime
inline uint64_t isPrime( uint64_t number )
{
 if ( ( (!(number & 1)) && number != 2 ) || (number < 2) )
    return 2;

 if(number % 3 == 0 && number != 3)
    return 3;

 //if(number<1373653)
 {
  for( uint64_t k = 1; 36*k*k-12*k < number;++k){
    if(number % (6*k+1) == 0){
        return (6*k+1);
    }
    if(number % (6*k-1) == 0){
        return (6*k-1);
    }
  }
  return 0;//prime
 }
/*
 if(number < 9080191)
 {
  if(witness(31,number)) return 1;
  if(witness(73,number)) return 1;
  return 0; //prime
 }


 if(witness(2,number)) return 1;
 if(witness(7,number)) return 1;
 if(witness(61,number)) return 1;
 return 0;//prime
*/
 /*WARNING: Algorithm deterministic only for numbers < 4,759,123,141 (uint64_t's max is 4294967296)
   if n < 1,373,653, it is enough to test a = 2 and 3.
   if n < 9,080,191, it is enough to test a = 31 and 73.
   if n < 4,759,123,141, it is enough to test a = 2, 7, and 61.
   if n < 2,152,302,898,747, it is enough to test a = 2, 3, 5, 7, and 11.
   if n < 3,474,749,660,383, it is enough to test a = 2, 3, 5, 7, 11, and 13.
   if n < 341,550,071,728,321, it is enough to test a = 2, 3, 5, 7, 11, 13, and 17.*/
}

/*
inline uint64_t isPrime( uint64_t number ){
    for(int i = 2; i < number/2; ++i){
        if((number%i)==0)
            return i;
    }
    return 0;
}
*/
///////////////////////////////////////////////////////////////////////////////


uint64_t getNumber(std::vector<bool>& output, int base){
    uint64_t res = 0;
    for(int i = 0; i < output.size(); ++i){
        if(output[i]){
            res += std::pow(base,i);
        }
    }
    return res;
}

void solveRec(std::vector<bool> output, int id, int& found, int to_found, std::ofstream& out_file){
    if(found >= to_found){
        return;
    }
    if(id == 0){
        std::vector<uint64_t> nums;
        std::vector<uint64_t> divs;
        bool valid = true;
        for(int b = 2; b <= 10 && valid; ++b){
            uint64_t num_to_check = getNumber(output,b);
            uint64_t divisor = isPrime(num_to_check);
            valid &= (divisor != 0);

            nums.push_back(num_to_check);
            divs.push_back(divisor);
        }

        if(valid){
            ++found;
            for(int i = 0; i < output.size(); ++i){
                if(output[output.size()-1-i]){
                    std::cout << '1';
                    out_file  << '1';
                }else{
                    std::cout << '0';
                    out_file  << '0';
                }
            }
            for(int i = 0; i < nums.size(); ++i){
                std::cout << " " << nums[i] << "(" << divs[i] << ")";
                out_file  << " " << divs[i];
            }

            std::cout << std::endl;
            out_file  << std::endl;
        }
    }else{
        output[id] = false;
        solveRec(output,id-1,found,to_found,out_file);
        output[id] = true;
        solveRec(output,id-1,found,to_found,out_file);
    }
}

int main(int argc, char *argv[]){

    std::ifstream in_file (argv[1]);
    std::ofstream out_file (argv[2]);

    int num_test_cases = 0;
    in_file >> num_test_cases;

    for(int i = 0; i < num_test_cases; ++i){
        int len,num_out;
        in_file >> len;
        in_file >> num_out;
        std::cout << len << std::endl;
        std::cout << num_out << std::endl;

        std::vector<bool> output(len,false);
        output[0] = true;
        output[len-1] = true;

        int found = 0;
        std::cout << "Case #" << i+1 << ":" << std::endl;
        out_file << "Case #" << i+1 << ":" << std::endl;
        solveRec(output,len-2,found,num_out,out_file);

        std::cout << "FOUND: " << found << std::endl;
    }


    return 0;
}
