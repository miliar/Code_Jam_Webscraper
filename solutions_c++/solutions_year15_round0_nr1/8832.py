//
//  main.cpp
//  Standing Ovation
//
//  Created by Jakub Powierza on 11.04.2015.
//  Copyright (c) 2015 Jakub Powierza. All rights reserved.
//

#include <iostream>
#include <stdio.h>

/*
1
6 0000109
 
4
4 11111
0 0
5 400011
5 000000
*/

int main(int argc, const char * argv[]) {
    // Testy
    int t = 0;
    scanf("%d\n", &t);
    
    // Wczytywanie testów
    for (int test = 1; test <= t; test++) {
        // Wczytywanie poziomu
        int s = 0;
        scanf("%d ", &s);
        
        // Wczytywanie ilości wszystkich poziomów
        char znak = 0;
        int ilosc = 0;
        int iloscLudziDoTejPory = 0;
        int iloscLudziZaproszonych = 0;
        scanf("%c", &znak);
        iloscLudziDoTejPory = (int)znak - 48;
        for (int niesmialosc = 1; niesmialosc <= s; niesmialosc++) {
            scanf("%c", &znak);
            ilosc = (int)znak - 48;
            if (ilosc != 0) {
                if (iloscLudziDoTejPory < niesmialosc) {
                    iloscLudziZaproszonych += niesmialosc - iloscLudziDoTejPory;
                    iloscLudziDoTejPory = niesmialosc;
                }
                iloscLudziDoTejPory += ilosc;
            }
        }
        scanf("%c", &znak);
        
        // Wypisanie wyniku
        printf("Case #%d: %d\n", test, iloscLudziZaproszonych);
    }
    
    return 0;
}
