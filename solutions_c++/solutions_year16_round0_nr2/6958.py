#include<cstdio>
#include<cstring>
#include<string>
using namespace std;
char cake[115];
char a[115];
int Case = 1;
int main(){
    int t;
    #ifndef ONLINE_JUDGE
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif
    scanf("%d\n",&t);
    while(t--){
        memset(a,0,sizeof(a));
        memset(cake,0,sizeof(cake));
        gets(cake);
        a[0] = cake[0];
        for(int i=1,j=0;i<strlen(cake);i++){
            if(cake[i]!=a[j])
                a[++j] = cake[i];
        }
        int i=0;
        while(a[i]!=0)
            i++;
        i--;
        if(a[i]=='-')
            printf("Case #%d: %d\n",Case++,i+1);
        else
            printf("Case #%d: %d\n",Case++,i);
    }
    return 0;
}
