#include<stdio.h>
#include<string.h>

int num(char a){
    return a-48;
}

int main()
{
    freopen("A-large.txt", "r",stdin);
    freopen("B.txt", "w",stdout);
    int n, maxi, sum,need;
    char str[1000];
    scanf("%d", &n);
    for(int i=1;i<=n;i++){
        sum=0;need=0;
        scanf("%d ", &maxi);
        scanf("%s", str);
        int k=strlen(str);
        for(int j=0;j<k;j++){
            if(num(str[j])){
                if(sum>=j)
                    sum+=num(str[j]);
                else{
                    need+=(j-sum);
                    sum+=(j-sum)+num(str[j]);
                }
            }
        }
        printf("Case #%d: %d\n",i,need);
    }
    return 0;
}
