/**
submitted by: prakhar8795
SLEEP. CODE. EAT. REPEAT.
**/
#include<stdio.h>
#include<string.h>

void solve()
{
    int test ;
    scanf("%d",&test) ;
    for(int k=0 ; k<test ; k++) {
        int smax ;
        scanf("%d",&smax) ;
        char input[smax+3] ;
        scanf("%s",input) ;
        int len=strlen(input),sum=input[0]-'0',ans=0 ;
        for(int i=1 ; i<len ; i++) {
            if(sum<i) {
                ans+=i-sum ;
                sum=i+(input[i]-'0');
            }
            else {
                sum+= input[i]-'0' ;
            }
        }
        printf("Case #%d: %d\n",k+1,ans) ;
    }
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("out.txt","w",stdout);
    #endif
    solve() ;
}
