#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

int main (){
    int t, n1, n2;
    scanf("%d", &t);
    FILE* out = fopen("a.txt", "w");
    for(int c=1; c<=t; c++){
        vector <bool>flag(16, false);
        scanf("%d", &n1);

        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                int a;
                scanf("%d", &a);
                if(i==n1-1){
                    flag[a-1] = true;
                }
            }
        }

        scanf("%d", &n2);
        int cnt = 0;
        int ans = 0;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                int a;
                scanf("%d", &a);
                if(i==n2-1){
                    if(flag[a-1] == true){
                            ans = a;
                            cnt++;
                    }
                }
            }
        }
        fprintf(out, "Case #%d: ", c);
        if(cnt==1){
            fprintf(out, "%d\n", ans);
        }
        else if(cnt==0){
            fprintf(out, "Volunteer cheated!\n");
        }
        else fprintf(out, "Bad magician!\n");
    }
}
