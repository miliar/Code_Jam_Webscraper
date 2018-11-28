#include<cstdio>
#include<algorithm>

using namespace std;

int main(){
    int T;
    scanf("%d",&T);
    for(int kk=1;kk<=T;kk++){
        int sm;
        char s[1006];
        scanf("%d %s",&sm,s);
        long long int sum=0,cnt=0;

        for(int i=0;i<=sm;i++){
            sum+=s[i]-'0';
            if(sum<i+1){
                cnt++;
                sum++;
            }
        }
        printf("Case #%d: %lld\n",kk,cnt);
    }
    return 0;
}
