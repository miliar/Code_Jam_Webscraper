#include<bits/stdc++.h>
using namespace std;
int main()
{

     freopen("D-small-attempt0 (1).in","r",stdin);
    freopen("out2.o","w",stdout);
    int test,u=1,i,j,k,l,m,n,s;
    scanf("%d",&test);
    while(test--){
            printf("Case #%d: ",u++);
        scanf("%d%d%d",&k,&l,&s);
        for(i=1;i<=s;i++){
            printf("%d",i);
            if(i<s)cout<<" ";
        }
        cout<<endl;
    }

}
