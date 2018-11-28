#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstring>
using namespace std;


map<char, map<char, string> > table;

void make_table(){
    table['1']['1'] = "1";
    table['1']['i'] = "i";
    table['1']['j'] = "j";
    table['1']['k'] = "k";

    table['i']['1'] = "i";
    table['i']['i'] = "-1";
    table['i']['j'] = "k";
    table['i']['k'] = "-j";

    table['j']['1'] = "j";
    table['j']['i'] = "-k";
    table['j']['j'] = "-1";
    table['j']['k'] = "i";

    table['k']['1'] = "k";
    table['k']['i'] = "j";
    table['k']['j'] = "-i";
    table['k']['k'] = "-1";
}


char pre[10000][10000];

int main(){
    make_table();
    int T;
    char cbuffer[10010];
    scanf("%d", &T);

    for(int tcase=1; tcase <= T; ++tcase){
        memset(pre, 0, sizeof(pre));
        fprintf(stderr, "%d\n", tcase);
        int length, repeat;
        scanf("%d %d", &length, &repeat);
        scanf("%s", cbuffer);
        string ss, _ss = cbuffer;
        for(int i=0; i < repeat; ++i){
            ss += _ss;
        }
        int n = ss.length();
        for(int i=0; i < n; ++i){
            char a = ss[i];
            pre[i][i] = a;
            bool minus = false;
            for(int j=i + 1; j < n; ++j){
                string& t = table[a][ss[j]];
                if(t.length() == 2){
                    minus = minus ? false : true;
                    a = t[1];
                }
                else{
                    a = t[0];
                }
                if(!minus){
                    pre[i][j] = a;
                }
            }
        }
        bool found = false;
        for(int i=0; i < n; ++i){
            if(pre[0][i] != 'i') continue;
            for(int j=i + 1; j < n - 1; ++j){
                if(pre[i + 1][j] != 'j') continue;
                if(pre[j + 1][n - 1] == 'k') {
                    found = true;
                    break;
                }
            }
            if(found)
                break;
        }
        if(found)
            printf("Case #%d: YES\n", tcase);
        else
            printf("Case #%d: NO\n", tcase);
    }
}

