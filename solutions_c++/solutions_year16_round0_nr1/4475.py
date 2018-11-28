//
//  main.cpp
//  ALarge
//

#include <iostream>

using namespace std;

FILE *f, *f2;

void getDigits(int digits[], long n, int &c) {
    
    while(n != 0) {
        
        int digit = n % 10;
        
        if (digits[digit] == 0) {
            digits[digit] = 1;
            c++;
            
        }
        
        
        n /= 10;
    }
    
}


int main(int argc, const char * argv[]) {
    // insert code here...
    int nr_cases;
    int n;
    f = fopen("/Users/Home/Work/CodeJam/QualificationRound/ALarge/ALarge/in.txt", "r");
    f2 = fopen("/Users/Home/Work/CodeJam/QualificationRound/ALarge/ALarge/out.txt", "w");
    
    
    if (f != NULL) {
        fscanf(f, "%d", &nr_cases);
        
        for (int i = 1; i <= nr_cases; i++) {
            int digits[10] = {0};
            int c = 0;
            long k = 0;
            
            fscanf(f, "%d", &n);
            cout<<"n = "<<n<<endl;
            
            fprintf(f2, "Case #%d: ", i);
            
            if (n == 0){
                
                fprintf(f2, "%s \n", "INSOMNIA");
                continue;
                
            }
            
            while (c != 10) {
                k++;
                getDigits(digits, n * k, c);
            }
            
            fprintf(f2, "%ld", n * k);
            
            /*         for (int i = 0; i < n; i++) {
             
             } */
            
            fprintf(f2, "\n");
            
        }
        
    } else {
        
        cout <<"Error: folder is NULL"<<endl;
    }
    
    cout <<"Done"<<endl;
    return 0;
}
