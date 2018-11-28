#include <bits/stdc++.h>
#define ll long long
using namespace std;

FILE * in;
FILE * out;

int T;
char buffer[2500];
string s,r;

int main() {
    in = fopen("input.in","r");
    out = fopen("output.out","w");

    fscanf(in,"%d",&T);

    for(int k=1;k<=T;k++) {
        fscanf(in,"%s",buffer);
        s = buffer;
        r = "";
        r += s[0];

        for(int i=1;i<s.size();i++)  {
            if(s[i] >= r[0])
                r = s[i] + r;
            else
                r = r + s[i];
        }

        fprintf(out,"Case #%d: %s\n",k,r.c_str());
    }


    return 0;
}
