#include <bits/stdc++.h>
using namespace std;

#define GCJ false

int N;
int sen[1002];

void solve(){
memset (sen,0,sizeof sen);
    scanf ("%d",&N);
    for (int i=0;i<N;i++){
        scanf ("%d",&sen[i]);
        //printf ("%d ",sen[i]);
    }
    //printf ("N\n");

        int onecnt=0,onesennum=0;
        for (int i=0;i<N;i++){
            if (sen[i]==1) onecnt++,onesennum=i;

        }
        if (onecnt==3){
            printf ("%c ",'A'+onesennum);
            sen[onesennum]--;
        }

    //int mxc=0;
    while (true){
        //mxc++;
        //if (mxc>10) break;
        int maxid,maxid2;
        maxid = maxid2 = -1;
        for (int i=0;i<N;i++){
            if (maxid==-1||sen[maxid]<=sen[i]) maxid = i;
        }
        for (int i=0;i<N;i++){
            if (maxid2==-1||maxid==maxid2||(sen[maxid2]<=sen[i]&&i!=maxid)) maxid2 = i;
        }
        if (maxid!=maxid2&&sen[maxid]>0&&sen[maxid2]>0){
            printf ("%c%c ",'A'+maxid,'A'+maxid2);
            sen[maxid]--;
            sen[maxid2]--;
        }
       /* if (maxid == maxid2){
            printf ("%d %d\n",sen[maxid],sen[maxid2]);
        }*/
        //int onecnt=0,onesennum=0;
        onecnt = 0;
        onesennum = 0;
        for (int i=0;i<N;i++){
            if (sen[i]==1) onecnt++,onesennum=i;

        }
        if (onecnt==3){
            printf ("%c ",'A'+onesennum);
            sen[onesennum]--;
        }
        bool Fin = true;
        for (int i=0;i<N;i++){
            if (sen[i]) Fin = false;
        }
        if (Fin) break;
        //printf ("%d %d %d %d\n",maxid,maxid2,sen[maxid],sen[maxid2]);
        //for (int i=0;i<N;i++){
        //    printf ("%d : %d\n",i,sen[i]);
        //}
    }
    printf ("\n");
}

int main(){


    if (!GCJ){
        freopen ("A-small-attempt1.in","r",stdin);
        freopen ("A-small-attempt1.out","w",stdout);
    }
    int TC;
    scanf ("%d",&TC);
    for (int tc=1;tc<=TC;tc++){
        printf ("Case #%d: ",tc);
        solve();
    }

return 0;
}
