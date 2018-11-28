#include <iostream>
#include <cstdio>

using namespace std;
int main()
{
    int cas=0,t,i,j,count,a,b;
    freopen("in.txt","r",stdin);
    freopen("c-output.txt","w",stdout);
    scanf("%d",&t);
    //unsigned
    int tw[]={1,2,4,8,16,32,64,128,256,512,1024};
    while(cas++<t){
        scanf("%d/%d",&a,&b);
        printf("Case #%d: ",cas);
        if(__builtin_popcount(b) != 1)
            printf("impossible\n");
        else{
            for(i=0;a >= tw[i];i++){

            }
            for(j=i;b != tw[j];j++){

            }
            printf("%d\n",j-i+1);

        }


    }
    return 0;
}
