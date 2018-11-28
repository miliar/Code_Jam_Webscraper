//
//  main.cpp
//  GoogleCodeJam
//
//  Created by FBE on 4/8/16.
//  Copyright © 2016 FBE. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;


int main(int argc, const char * argv[]) {
    long n, t, cont = 0, r=0;
    scanf("%li", &t);
    string str;
    while (t--) {
        cont++;
        scanf("%li", &n);
        bool numeros[10]{false};
        bool result = false;
        int j = 0;
        bool bandera = false;
        if (n == 0) {
            bandera = true;
            result = false;
        }
        while (bandera == false) {
            j++;
            r = j * n;
            str =to_string(r);
            for (int i = 0; i < str.length(); i++) {
                numeros[str[i] - '0'] = true;
            }
            int c = 0;
            for (int i = 0; i < 10; i++) {
                if (numeros[i]) {
                    c++;
                }
            }
            
            if (c == 10) {
                result = true;
                bandera = true;
            }
        }
        
        if (result) {
            printf("Case #%li: %li\n", cont, r);
        }else
            printf("Case #%li: INSOMNIA\n", cont);
    }
    return 0;
}
