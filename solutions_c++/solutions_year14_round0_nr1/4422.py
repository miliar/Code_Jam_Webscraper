#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>

#define FI first
#define SE second
#define MP make_pair
#define PB push_back

const int MAXN = 100005;

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;

int a[2][6][6];

int main(){
    int t;
    scanf("%d", &t);
    for (int tnum=1; tnum<=t; tnum++){
        int ans1, ans2;
        scanf("%d", &ans1);
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++)
                scanf("%d", &a[0][i][j]);
                
        scanf("%d", &ans2);
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++)
                scanf("%d", &a[1][i][j]);
        
        int ans = -1;
        for (int i=1; i<=16; i++){
            bool in1 = false, in2 = false;
            for (int k=1; k<=4; k++) if (a[0][ans1][k]==i) in1 = true;
            for (int k=1; k<=4; k++) if (a[1][ans2][k]==i) in2 = true;
            if (in1 && in2){
                if (ans==-1) ans = i;
                else {
                    ans = 0;
                    break;
                }
            }
        }
            
        printf("Case #%d: ", tnum);            
        if (ans==-1) printf("Volunteer cheated!\n");
        else
            if (ans==0) printf("Bad magician!\n");
            else
                printf("%d\n", ans);
    }
    return 0;
}
