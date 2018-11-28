


#include <cstdio>
#include <iostream>

using namespace std;

int main(int argc, char** argv) 
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int invites = 0;
        int atten = 0;
        
        int max;
        string word;
        
        cin >> max;
        cin >> word;

        for (int shy = 0; shy <= max; shy++) {            
            int dif = shy - atten;

            if (dif > 0) {
                invites += dif;
                atten += dif;
            }


            atten += word[shy] - '0';

            //printf("attend: %d, shy: %d, invites: %d\n", atten, shy, invites);
        }
        
        printf("Case #%d: %d\n", i+1, invites);
    }


}
