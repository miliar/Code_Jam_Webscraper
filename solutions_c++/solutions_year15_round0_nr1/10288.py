#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;
int getNP(char str[], int k){//getNumberOfPeople
    return str[k]-'0';
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int NCASE;
    scanf("%d",&NCASE);
    for(int TCASE=1; TCASE<=NCASE; TCASE++){
        int n, ans=0, sum=0;
        char inp[1001];
        scanf("%d%s",&n,inp);

        sum = getNP(inp, 0);
        for(int i=1; i<=n; i++){
            if(getNP(inp, i)>0){
                if(sum < i){
                    int nAdd = i-sum;
                    ans += nAdd;
                    sum += getNP(inp, i)+nAdd;
                }
                else
                    sum += getNP(inp, i);
            }
        }
        printf("Case #%d: %d\n",TCASE,ans);
    }
    return 0;
}
