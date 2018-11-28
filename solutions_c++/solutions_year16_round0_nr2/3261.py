    #include <bits/stdc++.h>
#define ll long long
#define fs first
#define sn second
using namespace std;

FILE * in;
FILE * out;

int t,r;
char str[250];

int main() {
    in = fopen("input.in", "r");
    out = fopen("output.out", "w+");

    fscanf(in,"%d",&t);

    for(int k=1;k<=t;k++) {
        fprintf(out,"Case #%d: ",k);

        fscanf(in,"%s",str);
        r = 0;

        int pj=strlen(str)-1;

        while(str[pj]=='+')
            pj--;

        if(pj >= 0) {
            char c = str[0];
            for(int i=0;i<=pj;i++) {
                if(str[i] != c) {
                    c = str[i];
                    r++;
                }
            }
            fprintf(out,"%d",r+1);
        }
        else {
            fprintf(out,"0");
        }



        fprintf(out,"\n");
    }

    return 0;
}
