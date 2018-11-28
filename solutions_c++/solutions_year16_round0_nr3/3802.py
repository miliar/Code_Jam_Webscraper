//
//  main.cpp
//  CSmall
//

#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

FILE *f, *f2;

#define LOW 200

void computeOtherBase(unsigned long number, vector<char> &charac, int base) {

    int digit;
    
    while(number != 0){
        digit = (number%base); /* remainder of x when divided by y */
        number = (number/base); /* x divided by y */
        charac.push_back(digit + '0');
       // otherBaseNumber += digit * k;
      //  k *= 10;
    }
    
    reverse(charac.begin(), charac.end());
  //  return otherBaseNumber;
    
}


unsigned long long computeOtherBaseStrange(unsigned long number, vector<char> &charac, int base) {
    
    int digit;
    int k = 0;
    unsigned long long otherBaseNumber = 0;
    
    
    for(int i = charac.size() - 1; i >= 0; i--) {
        
        digit = charac[i] - '0';
        otherBaseNumber += pow(base, k) * digit;
        k++;
    }
    
    return otherBaseNumber;
    
}

unsigned long computeDivisors(unsigned long long number) {

    
    for (unsigned long i = 2; i <= LOW; i++) {
        if (number % i == 0) {
                return i;
        }
        
    }
    return 0;
    
}

void computeBinaryNumber(int nr_bits, int j) {

    unsigned int max = pow(2, nr_bits) - 1;
    unsigned int max2 = pow(2, nr_bits + 1);
    unsigned long finalNumberBase2 = 0;
    unsigned long finalNumberBase10 = 0;
    unsigned long long otherBaseNumber = 0;
    unsigned long long vectorBase[11] = {0};
    unsigned long divisors[11] = {0};
    unsigned int i = 0;
    bool isPrime = false;
    vector<char> charac;
    
    
    while(i <= max && j > 0) {
        charac.clear();
        isPrime = false;
        finalNumberBase2 = 0;
        finalNumberBase10 = 0;
        otherBaseNumber = 0;
        memset(vectorBase, 0, sizeof(unsigned long long) * 11);
        memset(divisors, 0, sizeof(unsigned long) * 11);
        
        finalNumberBase2 = i << 1 | 1;
        finalNumberBase2 = finalNumberBase2 | max2;
        
        computeOtherBase(finalNumberBase2, charac, 2);
        
        for(int base = 2; base <= 10; base++) {
        
            otherBaseNumber = computeOtherBaseStrange(finalNumberBase10, charac, base);
            vectorBase[base] = otherBaseNumber;
            divisors[base] = computeDivisors(otherBaseNumber);
            
            if (divisors[base] == 0) {
                isPrime = true;
                break;
            }
        }
            
            i++;
            if (isPrime) continue;
        
            std::string str(charac.begin(), charac.end());
            
            fprintf(f2, "%s " , str.c_str());
            cout<<"j = "<<j <<endl;
        
        for (int base = 2; base <= 10; base++) {
                fprintf(f2, "%lu ", divisors[base]);
            }
            
            fprintf(f2, "\n");

            j--;
    }
    

    if (j != 0) {
        cout <<"ERROR!"<<endl;
    }
    
}


int main(int argc, const char * argv[]) {
    // insert code here...
    int nr_cases, n, j;
    f = fopen("/Users/Home/Work/CodeJam/QualificationRound/CSmall/CSmall/in.txt", "r");
    f2 = fopen("/Users/Home/Work/CodeJam/QualificationRound/CSmall/CSmall/out.txt", "w");
    
    
    if (f != NULL) {
        fscanf(f, "%d", &nr_cases);
     
        for (int i = 1; i <= nr_cases; i++) {
            fscanf(f, "%d %d", &n, &j);
            fprintf(f2, "Case #%d: \n", i);
            computeBinaryNumber(n-2, j);
        }
        
    } else {
        
        cout <<"Error: folder is NULL"<<endl;
    }
    
    cout<<"Done"<<endl;
    return 0;
}