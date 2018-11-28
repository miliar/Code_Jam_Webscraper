//
//  main.cpp
//  BSmall


#include <iostream>
#include <vector>

using namespace std;

FILE *f, *f2;

bool myfunction (int i,int j) { return (i<j); }

void solve(int s[], int n) {
    
    int heights[2600] = {0};
    vector<int> missing_vector;

    for (int i = 0; i < n * (2 * n - 1); i++) {
    
        heights[s[i]]++;
    }
    
    for (int i = 0; i < 2600; i++) {
    
        if (heights[i] % 2 == 1) {
            missing_vector.push_back(i);
            
        }
    }
    
    std::sort(missing_vector.begin(), missing_vector.end(), myfunction);
    
    for (int i = 0; i < missing_vector.size();i++) {
    
        fprintf(f2, "%d ", missing_vector[i]);
    }
    
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int nr_cases, n;
    f = fopen("/Users/Home/Work/CodeJam/Round 1A/BSmall/BSmall/in.txt", "r");
    f2 = fopen("/Users/Home/Work/CodeJam/Round 1A/BSmall/BSmall/out.txt", "w");
    
    int s[1000000];
    
    if (f != NULL) {
        fscanf(f, "%d", &nr_cases);
        
        for (int i = 1; i <= nr_cases; i++) {
            fscanf(f, "%d", &n);
            
            for (int i = 0; i< n * (2 * n - 1); i++) {
            
                fscanf(f, "%d", &s[i]);
            }
            
            
         /*   for (int i = 0; i< n * (2 * n - 1); i++) {
                
                printf("%d ", s[i]);
            } */
            
            fprintf(f2, "Case #%d: ", i);
            solve(s, n);
            
            fprintf(f2, "\n");
            
        }
        
    } else {
        
        cout <<"Error: folder is NULL"<<endl;
    }
    
    cout <<"DONE"<<endl;
    return 0;
}