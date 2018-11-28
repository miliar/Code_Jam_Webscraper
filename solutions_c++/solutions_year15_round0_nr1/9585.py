//
//  main.cpp
//  StandingO
//
//  Created by haberlan on 4/11/15.
//  Copyright (c) 2015 haberlan. All rights reserved.
//

#include <stdlib.h>
#include <stdio.h>

int main (int argc, char **argv)
{
    unsigned int T = 0;
    scanf ("%u", &T);
    unsigned int Tc = T+1;
    
    while (T > 0)
    {
        unsigned int sMax;
        unsigned int minShy;
        bool notShy = true;
        char aud[1024];
        unsigned int invites = 0;
        unsigned int members = 0;
        scanf("%u %s", &sMax, aud);
        minShy = sMax;
        for (unsigned int n=0; n <= sMax; n++)
        {
            unsigned int numAud = (aud[n] - '0');
            if (numAud)
                if (n > members)
                {
                    invites += n - members;
                    members += n - members;
                }
            members += numAud;
        }
//        printf("%u %u\n", members, invites);
        if (sMax > members)
            invites += sMax - members;

        printf("Case #%u: %u\n", Tc-T, invites);
        T--;
    }
}