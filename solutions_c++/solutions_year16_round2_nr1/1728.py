#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

char base[][10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int order[] = {0, 2, 4, 6, 5, 7, 8, 1, 9, 3};
char identifier[] = "ZWUXFVGOIT";
int siz[] = {4, 3, 3, 5, 4, 4, 3, 5, 5, 4};
int hah[305];
char inp[2005];
vector<int> ans;

int main(){
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int totalCase;
    scanf("%d", &totalCase);
    for(int T = 1; T <= totalCase; ++T){
        ans.clear();
        int len = 0;
        scanf("%s", inp);
        for(len = 0; inp[len] != NULL; ++len)
            hah[inp[len]]++;
        for(int i = 0; i < 10; ++i){
            int have = hah[identifier[i]];
            if(!have)
                continue;
            for(int j = 0; j < siz[order[i]]; ++j)
                hah[base[order[i]][j]]-=have;
            for(int j = 0; j < have; ++j)
                ans.push_back(order[i]);
        }
        sort(ans.begin(), ans.end());
        printf("Case #%d: ", T);
        for(int i = 0; i < ans.size(); ++i)
            printf("%d", ans[i]);
        printf("\n");
    }
    return 0;
}
/*
4
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER

3
RNEHESIVENEETN
FOIEEVVSRXNSFEUI
OEZUROOFETRHRENE
*/
