#include <iostream>
#include <cstdio>

using namespace std;

int main()
{

    //freopen("A-large.in","r",stdin);
    //freopen("test.txt","r",stdin);
    //freopen("A-large.out","w",stdout);
    int smax,i,T,j,nf,cumul;
    string tmp;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
        nf = 0;
        cumul = 0;
        scanf("%d",&smax);

        cin >> tmp;
        for(j=0;j<=smax;j++){

            if(cumul<j){
                nf += j-cumul;
                cumul = j;
            }
            if(tmp[j]!='0')
                cumul+=tmp[j]-'0';



        }
        printf("Case #%d: %d\n",i,nf);
    }
    return 0;
}
