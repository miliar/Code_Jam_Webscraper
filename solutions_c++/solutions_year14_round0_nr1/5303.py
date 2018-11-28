#include <cstdio>
#include <set>
using namespace std;
void solve(int T) {
    printf("Case #%d: ",T);
    set<int> S;
    int a[4],b[4],ans1,ans2,tmp;
    scanf("%d",&ans1);
    for(int i=1;i<=4;i++) {
        if(i==ans1) {
            for(int j=0;j<4;j++) scanf("%d",&a[j]);
        }else {
            for(int j=0;j<4;j++) scanf("%d",&tmp);
        }
    }
    scanf("%d",&ans2);
    for(int i=1;i<=4;i++) {
        if(i==ans2) {
            for(int j=0;j<4;j++) scanf("%d",&b[j]);
        }else {
            for(int j=0;j<4;j++) scanf("%d",&tmp);
        }
    }
    for(int i=0;i<4;i++) {
        for(int j=0;j<4;j++) {
            if(a[i]==b[j]) S.insert(a[i]);
        }
    }
    if(S.size()==0) printf("Volunteer cheated!\n");
    else if(S.size()==1) printf("%d\n",*(S.begin()));
    else printf("Bad magician!\n");
}
int main() {
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++) {
        solve(i);
    }   
}
