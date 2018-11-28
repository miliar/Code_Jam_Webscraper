#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>

#define I 2
#define J 3
#define K 4
int mul[5][5] = {{0,0,0,0,0},
                 {0,1,I,J,K},
                 {0,I,-1,K,-J},
                 {0,J,-K,-1,I},
                 {0,K,J,-I,-1}};
int div[5][5] = {{0,0,0,0,0},
                 {0,1,-I,-J,-K},
                 {0,I,1,K,-J},
                 {0,J,-K,1,I},
                 {0,K,J,-I,1}};
using namespace std;
char ch[10010];
int res[10010];
vector<int> s1, s2;
int division(int st, int en) {
    int sign = 1;
    if (res[st] <0) sign *= -1;
    if (res[en] <0) sign *= -1;
    return sign*div[abs(res[en])][abs(res[st])];
}
void Solve(int no) {
    int L, X;
    int re = 1;
    s1.clear();
    s2.clear();
    scanf("%d %d\n", &L, &X);
    for (int i=0; i<L; i++) {
        scanf("%c", ch+i);
    }
    res[0] = ch[0]-'g';
    if (res[0] == I) s1.push_back(0);
    for (int i=1; i<L*X; i++) {
        res[i] = mul[abs(res[i-1])][ch[i%L]-'g'];
        if (res[i-1]<0) res[i] *= -1;
        if (res[i] == I) s1.push_back(i);
    }
    if ((L*X < 3) || (res[L*X-1] != -1)) {
        printf("Case #%d: NO\n", no);
        return;
    }
    for (int i=L*X-2; i>=0; i--) {
        if (division(i, L*X-1) == K) s2.push_back(i);
    }
if (0) {
cout << "-===========" << endl;
for (int i=0; i<s1.size(); i++)
    cout << s1[i] << " ";
cout << endl;
for (int j=0; j<s2.size(); j++)
cout << s2[j] << " ";
cout << "==============" << endl;

}
    for (int i=0; i<s1.size(); i++) {
        for (int j=0; j<s2.size(); j++) {
            if (s1[i] >= s2[j]) break;
            if (division(s1[i], s2[j]) == J) {
                printf("Case #%d: YES\n", no);
                return;
            }
        }
    }
    printf("Case #%d: NO\n", no);
    
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i=0; i<T; i++) {
        Solve(i+1);
    }
    
}