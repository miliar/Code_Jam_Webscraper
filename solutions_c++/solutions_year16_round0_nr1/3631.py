#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,x,n,tmp;
    scanf("%d", &t);
    for(int j=1; j<=t; ++j){
        set<int> s;
        scanf("%d", &n);
        for(int i=1;i<=1000000 ;i++){
            x = i*n;
            if(i!=1)
            if(tmp==x){
                printf("Case #%d: INSOMNIA\n", j);
                break;
            }
            tmp = x;
            while(tmp){
                s.insert(tmp%10);
                tmp = tmp/10;
            }
            if(s.size()==10){
                printf("Case #%d: %d\n", j,x);
                break;
            }
        }
    }
    return 0;
}
