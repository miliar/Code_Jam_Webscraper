/*
    https://code.google.com/codejam/contest/2437488/dashboard#s=p0
*/
#include <iostream>
#include <cstdio>

using namespace std;

#define MAXNUM 1000000

int seq[MAXNUM];

int main()
{
    int T, L, n;
    
    scanf("%d\n", &T);
     
    int num = 1;

    while (T--) {
        char ch;
        
        for (int i = 0; i < MAXNUM; i++)
            seq[i] = 0;
            
        L = 0;

        int start = 0;
        int conseq = 0;
        
        while (true) {
            scanf("%c", &ch);
            
            if (ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u' && ch != ' ') { // consonants
                if (conseq == 0)
                    start = L;
                conseq++;
            } else { // vowels
                if (conseq > 0) {
                    seq[start] = conseq;
                    
                    //cout << "start: " << start << " conseq: " << conseq << endl;
                    conseq = 0;
                }
            }
            
            if (ch == ' ')
                break;

            L++;
        }
        scanf("%d\n", &n);
        //cout << "L: " << L << " n: " << n << endl;
        
        start = 0;
        
        int remain = L;
        int ans = 0;
        
        for (int i = 0; i < L; i++) {
            for (int j = i; j < L; j++) {
                if (seq[j] >= n) {
                    //cout << "i: " << i << " j: " << j << " seq: " << seq[j] << " front: " << j-i+1 << " after: " << L-j-n+1 << " add: " << (j-i+1)*(L-j-n+1) << endl;
                    ans += (j - i + 1) * (L - j - n + 1);
                    seq[j+1] = seq[j] - 1;
                    seq[j] = 0;
                    i = j;
                    break;
                }
            }
        }
        cout << "Case #" << (num++) << ": " << ans << endl;
    }
    
    return 0;
}
