#include <cstdio>
#include <vector>
using namespace std;


int T, guess, tmp;

int main() {
    
    scanf("%d\n", &T);
    for (int x = 0; x < T; x++) {
        int f[17] = {0};
        
        for (int k = 0; k < 2; k++) {
            scanf("%d\n", &guess);
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    scanf("%d", &tmp);
                    if (i + 1 == guess) f[tmp]++;
                }
                scanf("\n");
            }
        }
        vector<int> ans;
        for (int i = 1; i <= 16; i++) if (f[i] == 2) 
            ans.push_back(i);

        if (ans.size() == 1) 
            printf("Case #%d: %d\n", x + 1, ans[0]);
        else if (ans.size() == 0)
            printf("Case #%d: Volunteer cheated!\n", x + 1);
        else printf("Case #%d: Bad magician!\n", x + 1);
    }
    
    return 0;
}
