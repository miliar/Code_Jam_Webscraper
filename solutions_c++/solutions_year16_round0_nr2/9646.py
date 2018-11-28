#include <cstdio>
#include <iostream>

using namespace std;

int T;
int main(){
    freopen("flipping.in", "r", stdin);
    freopen("flipping.out", "w", stdout);
    fscanf(stdin, "%d", &T);
    for (int i = 0; i < T; i++){
        char a[110];
        // for (int j = 0; j < 110; j++){
        //     char a[j] = 'n';
        // }
        fscanf(stdin, "%s", a);
        char curr = a[0];
        int counter = 1;
        int changes = 0;
        while(a[counter]){
            if (a[counter] != curr){
                curr = a[counter];
                changes++;
            }

            counter++;
        }
        if (a[counter-1] == '-'){
            changes++;
        }
        fprintf(stdout, "Case #%d: %d\n", i+1, changes);
    }

}