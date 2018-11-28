#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int main() {
    double naomi[1000], ken[1000];
    int T, len, war, dwar;

    cin >> T;

    for(int ix = 1; ix <= T; ix++) {
        cin >> len;

        for(int iy = 0; iy < len; iy++)
        	cin >> naomi[iy];

        for(int iy = 0; iy < len; iy++)
        	cin >> ken[iy];

        sort(naomi, naomi+len);
        sort(ken, ken+len);

        /*cout << "Nao: ";
        for(int iy = 0; iy < len; iy++)
            printf("%.3f ", naomi[iy]);
        cout << endl;

        cout << "Ken: ";
        for(int iy = 0; iy < len; iy++)
        	printf("%.3f ", ken[iy]);
        cout << endl;*/



        dwar = war = 0;
        for(int np = 0, kp = 0; kp < len; kp++) {
            if(naomi[np] < ken[kp])
            	np++;

            if(kp+1 == len)
            	war = len-np;
        }

        for(int np = 0, kp = 0; np < len; np++) {
            if(naomi[np] > ken[kp])
            	kp++;

            if(np+1 == len)
            	dwar = kp;
        }

        cout << "Case #" << ix << ": " << dwar << " " << war << endl;
    }

    return 0;	
}
