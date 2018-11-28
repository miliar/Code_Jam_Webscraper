//Counting Sheep
#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
    //freopen("input.txt", "r", stdin);
    
    int T;
    scanf("%d", &T);
    
    for (int i=1; i<=T; i++) {
        int N;
        scanf("%d", &N);
        
        if(!N) {
            cout << "Case #" << i << ": INSOMNIA\n";
            continue;
        }
        
        bool flag[10];
        for(int k=0; k<10; k++) flag[k]=false;
        int count=0;
        
        int j;
        int D;
        for (j=1; count<10;j++){
            unsigned long long M=j*N;
            while(M){
                int d=M%10;
                if(!flag[d]) {
                    flag[d] = true;
                    count++;
                }           
                M /= 10;
            }
            D = j*N;
        }
        
        cout << "Case #" << i << ": " << D << endl;
    }
    
    return 0;
}
