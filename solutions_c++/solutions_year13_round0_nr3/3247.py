#include<cstdio>
#include<algorithm>
#include<fstream>
using namespace std;
const int NN = (int)1e7;
typedef long long LL;
int tt,d[50];
LL a[101];
bool huw(LL i) {
    int l;
    for (l = 0; i; i /= 10) d[l++] = i % 10;
    for (int j = 0; j < l; ++j) if (d[j] != d[l-j-1]) return 0;
    return 1;
}
void load() {
    ifstream fin("data_c.log");
    if (fin.rdstate() == ios::goodbit) {
        while (fin.rdstate() == ios::goodbit) fin>> a[tt++];
        return ;
    }
    fin.close();
    for (int i = 1; i <= NN; ++i) 
        if (huw((LL)i) && huw(i * (LL)i)) a[tt++] = i * (LL)i;
    ofstream fou("data_c.log");
    for (int i = 0; i < tt; ++i) fou<< a[i]<< '\n';
    fou.close();
}
int TT,mm,l,r;
int main() {
    load();
    a[tt] = ((LL)1) << 57;
    for (scanf("%d", &TT), mm = TT; TT; --TT) {
        printf("Case #%d: ", mm-TT+1);
        scanf("%I64d%I64d", &l, &r);
        r = upper_bound(a, a + tt, r) - a;
        l = lower_bound(a, a + tt, l) - a;
        printf("%d\n", r - l);
    }
    return 0;
}
