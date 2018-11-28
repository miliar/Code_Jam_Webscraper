#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out1.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    char ans[3005];
    for(int k=1; k<=t; k++){
        char S[1005];
        cin>>S;
        int p=1500, q=1500;
        int s=strlen(S);
        for(int i=0; i<s; i++){
            if(i==0)
            {
                ans[p]=S[i];
            }
            else{
                if(S[i]<ans[p]){
                    ans[++q]=S[i];
                }
                else{
                    ans[--p]=S[i];
                }
            }
        }

        printf("Case #%d: ", k);
        for(int i=p; i<=q; i++){
            printf("%c", ans[i]);
        }
        printf("\n");
    }

    return 0;
}
