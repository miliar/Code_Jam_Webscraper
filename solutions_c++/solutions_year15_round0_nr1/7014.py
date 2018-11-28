#include <stdio.h>

using namespace std;

int main()
{

    freopen("A-large.in","r+",stdin);
    freopen("A-large.out","w+",stdout);
    int t,n;
    char cad[1234];
    scanf("%d",&t);
    for (int i=1; i<=t; i++){
        scanf("%d",&n);
        scanf("%s",cad);
        int sum=cad[0]-'0';
        int cont=0;
        for (int j=1; j<=n; j++){
            if (cad[j]>'0' && j>sum){
                cont+=(j-sum);
                sum+=(j-sum);
            }
            sum+=(cad[j]-'0');
        }
        printf("Case #%d: %d\n",i,cont);
    }
    return 0;
}
