
#include<iostream>
#include<set>
#include<stdio.h>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("data.out","w",stdout);
    int T;
    scanf("%d",&T);
    set<int> s;
    int j=1;
    while(j<=T){
        int N;
        scanf("%d",&N);
        int res=N;
        if(N==0)
            printf("Case #%d: INSOMNIA\n",j);
        else{
            int i=0;
            while(++i && s.size()!=10){
                N=res*i;
                int tmp=N;
                int a;
                while(tmp!=0){
                    a=tmp%10;
                    if(s.find(a)==s.end())
                        s.insert(a);
                    tmp=tmp/10;
                }
            }
        printf("Case #%d: %d\n",j,N);
        s.clear();
        }
        j++;
    }
    return 0;
}
