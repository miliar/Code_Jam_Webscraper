#include<bits/stdc++.h>
using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
set<char>s;
long long sheep(int n){
    int i;
    long long res,x;
    for(i=1;;i++){
        x=i*n;
        while(x>0){
            s.insert(x%10);
            x/=10;
        }
        if(s.size()==10)
            return (i*n);
    }
}
int main()
{
    //READ("A-large.in");
    //WRITE("A-large.out");
    int i,t,n;
    scanf("%d", &t);

    for(i=1;i<=t;i++){
        scanf("%d",&n);
        if(n==0){
                printf("Case #%d: INSOMNIA\n",i);
        }
        else
            printf("Case #%d: %d\n",i,sheep(n));
        s.clear();
    }

}
