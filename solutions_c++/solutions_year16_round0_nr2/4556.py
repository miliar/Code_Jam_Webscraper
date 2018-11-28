//
//  main.cpp
//  BLarge

#include <iostream>

using namespace std;

FILE *f, *f2;

int main(int argc, const char * argv[]) {
    // insert code here...
    int nr_cases;
    char s[103];
    f = fopen("/Users/Home/Work/CodeJam/QualificationRound/BLarge/BLarge/in.txt", "r");
    f2 = fopen("/Users/Home/Work/CodeJam/QualificationRound/BLarge/BLarge/out.txt", "w");
    
    if (f != NULL) {
        fscanf(f, "%d", &nr_cases);
        
        for (int i = 1; i <= nr_cases; i++) {
            int c = 0;
            memset(s, 0, sizeof(char) * 103);
            fscanf(f, "%s", s);
            int k = 1;
            
            while(s[k] != '\0') {
                
                if (s[k-1] != s[k]) {
                    c++;
                }
                k++;
            }
            
            if (s[k - 1] == '-') {
                
                c++;
            }
            
            fprintf(f2, "Case #%d: ", i);
            fprintf(f2, "%d", c);
            
            
            fprintf(f2, "\n");
            
        }
        
    } else {
        
        cout <<"Error: folder is NULL"<<endl;
    }
    
    cout<<"Done"<<endl;
    return 0;
}
