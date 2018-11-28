#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;

    scanf("%d",&T);

    for(int I=1;I<=T;I++)
    {
        char save[10010];
        int S_max;
        scanf("%d %s",&S_max,save);

        int standing=save[0]-48,invite=0,F_invite=0;
        for(int J=1;J<=S_max;J++)
        {

            if(standing<J)
                invite=(J-standing);
                else invite=0;
                F_invite+=invite;
            //
            standing+=(save[J]-48)+invite;

            //printf("J=%d S=%d %d\n",J,standing,invite);
        }



        printf("Case #%d: %d\n",I,F_invite);
        //printf("final=%d\n",standing);
    }

    return 0;
}
