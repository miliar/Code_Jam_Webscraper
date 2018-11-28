#include <bits/stdc++.h>
using namespace std;
int main() {
    int t,shylevel,b=0,c=0,d=0,y=1;
    char a[1022];
    FILE *fp = fopen("out.txt", "w");
    cin >> t;
    while(t-->0) {
        cin >> shylevel;
        cin >> a;
           b += a[0]-'0';
           for(int x = 1;x <= shylevel; x++) {
                if(b < x) {
                d = x - b;
                c += d;
                b += d;
                }
                b += a[x] - '0';
            }
          // printf("Case #%d: %d\n",y,c);
           fprintf(fp, "Case #%d: %d\n",y,c);
           y++;
           d = 0;
           b = 0;
           c = 0;
    }
    fclose(fp);
    return 0;
}
