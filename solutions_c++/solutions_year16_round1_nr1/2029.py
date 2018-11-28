//
//  main.cpp
//  ASmall


#include <iostream>
#include <vector>

using namespace std;

FILE *f, *f2;


void solve(char s[]) {

    int i = 1;
    
    vector<char> s3;
    
    s3.push_back(s[0]);
    
    while(s[i] != '\0') {
        
        if (s[i] >= s3[0]) {
        
            s3.insert(s3.begin(), s[i]);
        } else {
        
            s3.push_back(s[i]);
        }
        
        i++;
    }
    
    s3[i] = '\0';
    
    char *s2 = &s3[0];
    
        fprintf(f2, "%s", s2);
    
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int nr_cases;
    char s[1005];
    f = fopen("/Users/Home/Work/CodeJam/Round 1A/ASmall/ASmall/in.txt", "r");
    f2 = fopen("/Users/Home/Work/CodeJam/Round 1A/ASmall/ASmall/out.txt", "w");
    
    if (f != NULL) {
        fscanf(f, "%d", &nr_cases);
        
        for (int i = 1; i <= nr_cases; i++) {
            fscanf(f, "%s", s);
            
            fprintf(f2, "Case #%d: ", i);
            solve(s);
            
            
            fprintf(f2, "\n");
            
        }
        
    } else {
        
        cout <<"Error: folder is NULL"<<endl;
    }
    
    cout<<"DONE"<<endl;
    return 0;
}