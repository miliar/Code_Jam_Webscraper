#include <stdio.h>
#include <vector>
#include <map>
#include <math.h>
using namespace std;
vector<int> fas;

bool isfair(int y) {
    long long x = 1ll*y*y;
    if (x<10) return true;

    static int digs[102];
    int len = 0;
    for (; x; x/=10) 
        digs[len++] = x%10;

    int i=0, j=len-1;
    while (i<j && digs[i] == digs[j]) ++i,--j;
    return i>=j;
}

void init() {
    vector<int> helper[5];
    for (int i=1; i<=9; ++i)
        helper[0].push_back(i);
    for (int i=1; i<=9; ++i)
        helper[1].push_back(i*11);
    for (int i=1; i<=9; ++i) 
        for (int j=0; j<=9; ++j)
            helper[2].push_back(i*101+j*10);
    for (int i=1; i<=9; ++i) 
        for (int j=0; j<=9; ++j)
            helper[3].push_back(i*1001+j*11);
    for (int i=10; i<=99; ++i)
        for (int j=0; j<=9; ++j)
            helper[4].push_back(i*1000+i/10+(i%10)*10+j*100);

    fas.push_back(0);
    fas.push_back(1);
    fas.push_back(2);
    fas.push_back(3);
    fas.push_back(11);
    fas.push_back(22);
    int tens=10;
    for (int i=0; i<5; ++i) {
        tens *= 10;
        int HLEN = helper[i].size();
        for (int k=1; k<=3; ++k) {
            int x = k*(tens+1);
            if (isfair(x)) fas.push_back(x);
            for (int j=0; j<HLEN; ++j) {
                x = k*(tens+1)+(tens/10)*helper[i][j];
                if (isfair(x)) fas.push_back(x);
            }
        }
    }
}

int solve(int x) {
    int r = sqrt(x);
    const int LEN = fas.size();
    for (int i=0, j=LEN-1; i<=j; ) {
        int m = i+(j-i)/2;
        if (fas[m] == r) return m+1;
        if (fas[m] >  r) {
            if (m>=1 && fas[m-1]<r) return m;
            else j=m-1;
        } else {
            if (m+1<LEN && fas[m+1]>r) return m+1;
            else i=m+1;
        }
    }
}

int main(int argc, char * argv[]) {
    init();
    int T;
    scanf("%d\n", &T);
    for (int k=1; k<=T; ++k) {
        int A, B;
        scanf("%d%d\n", &A, &B);
        printf("Case #%d: %d\n", k, solve(B)-solve(A-1));
    }
    return 0;
}
