#include<cstdio>
#include<string>
#include<string.h>
using namespace std;
char str[1000000];
string complete;

char* to_ch = "ijk";
int mem[3][128][2][10002];

char multiply[128][128];
int sign_multiply[128][128];

int calc(int what, char current, int neg, int index){
    //fprintf(stderr, "%c, %c, %d, %d\n", to_ch[what], current, neg, index);
    if (index == complete.size() && what == 2 && current == to_ch[what] && !neg)
        return 1;
    if (index >= complete.size() || what > 2)
        return 0;
    int& result = mem[what][(int) current][neg][index];
    if ( result != -1 ) return result;
    if ( calc(what, multiply[current][complete[index]], neg ^ sign_multiply[current][complete[index]], index + 1))
        return result = 1;
    if ( !neg && current == to_ch[what] && calc(what + 1, '1', 0, index))
        return result = 1;
    return result = 0;
}

int main(){
    int cnt = 0;
    string all = "1ijk";
    string temp = "1ijki1kjjk1ikji1";
    int temp_[] = {0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,1};
    for (int i = 0; i < all.size(); ++i)
        for (int j = 0; j < all.size(); ++j){
            multiply[all[i]][all[j]] = temp[cnt];
            sign_multiply[all[i]][all[j]] = temp_[cnt++];
        }
    int tc;
    scanf("%d", &tc);
    for (int T = 1; T <= tc; ++T){
        int l, x;
        scanf("%d %d %s", &l, &x, str);
        for (complete = ""; x--; complete += str) ;
        memset(mem, -1, sizeof mem);
        printf("Case #%d: %s\n", T, calc(0, '1', 0, 0) ? "YES" : "NO");
    }
    return 0;
}
