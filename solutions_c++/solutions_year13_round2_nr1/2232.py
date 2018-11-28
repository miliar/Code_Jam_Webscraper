#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;

ifstream sf("osmos.in");
ofstream vf("osmos.out");

long long int cs;
vector <int> sizes;
int n, t;

int main () {
    sf >> t;
    for (int k = 1; k <= t; k++) {
        int ch = 0;
        sf >> cs >> n;
        sizes.resize(n);
        for (int i = 0; i < n; i++) sf >> sizes[i];
        sort(sizes.begin(), sizes.begin() + n);
        for (int i = 0; i < n; i++) {
            if (sizes[i] < cs) {
                cs += sizes[i]; 
                //cout << "ate " <<sizes[i]<< ", now size " << cs << endl;
                continue;  
            }   
            int eat = 0;
            int temp = cs;
            while (temp <= sizes[i] && temp != 1) {
                temp += temp -1;
                eat++;   
            }  
            if (eat < n - i && temp != 1) {
                cs = temp + sizes[i];
                ch += eat;
                //cout << "ate " <<eat<< " times, now size " << cs << endl;
            }
            else {
                ch += n - i;
                //cout << "deleted " << n-i << endl;
                break;
            }
        }
        vf << "Case #" << k << ": " << ch << endl;   
    }
    //system("pause");
}
