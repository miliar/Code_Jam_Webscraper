#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

FILE *in = fopen("A.in","r");
FILE *out = fopen("A.out","w");
int cnt[17];
vector <int> ret;

void update () {
    int ans;
    fscanf (in,"%d",&ans);
    ans --;
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            int x;
            fscanf (in,"%d",&x);
            if (i == ans) {
                cnt[x] ++;
            }
        }
    }
}

int main () {
    int t,k=1;
    fscanf (in,"%d",&t);
    while (t --) {
        fprintf (out,"Case #%d: ",k++);
        memset (cnt,0,sizeof(cnt));
        ret.clear();
        update ();
        update ();
        for (int i=1; i<=16; i++) {
            if (cnt[i] == 2) {
                ret.push_back(i);
            }
        }
        int n = ret.size();
        if (n == 0) fprintf (out,"Volunteer cheated!\n");
        else if (n > 1) fprintf (out,"Bad magician!\n");
        else fprintf (out,"%d\n",ret[0]);
    }
}
