//Revenge of the Pancakes
#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
    //freopen("input.txt", "r", stdin);
    
    int T;
    scanf("%d", &T);
    
    for(int i=1; i<=T; i++) {
        char S[110];
        scanf("%s", S);
        int l=0;
        while (S[l] != '\0' && S[l] != '\n') l++;
        
        int j=l-1;
        int flips=0;
        while(j>=0 && S[j] == '+') j--;
        for(;j>=0;j--){
            if(S[j] == S[j+1]) {
                continue;
            }
            flips++;
        }
        
        cout << "Case #" << i << ": " << flips << endl;
    }
    
    return 0;
}
