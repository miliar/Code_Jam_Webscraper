//
//  main.cpp
//  Pro4
//
//  Created by dong on 4/10/16.
//  Copyright © 2016 dong. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    FILE *file = fopen("Pro4.txt", "w");
    
    int T;
    scanf("%d", &T);getchar();
    
    int K, C, S;
    for (int k = 1; k <= T; ++k) {
        scanf("%d %d %d", &K, &C, &S);getchar();
        fprintf(file, "Case #%d: ", k);
        fprintf(file, "1");
        for (int i = 2; i <= K; ++i) {
            fprintf(file, " %d", i);
        }
        fprintf(file, "\n");
    }
    
    fclose(file);
    return 0;
}
