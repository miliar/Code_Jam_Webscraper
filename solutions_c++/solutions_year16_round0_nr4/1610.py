#include <bits/stdc++.h>

using namespace std;

long long K,C,S;
vector <long long> anslist;

void clearmem(){
    anslist.clear();
}

void solve(){
    clearmem();
    scanf ("%I64d%I64d%I64d",&K,&C,&S);
    if (C>1){
        long long Kpc = 1,lenK;
        for (int i=1;i<C;i++)
            Kpc *= K;
        lenK = Kpc * K;
        //printf ("-> %I64d\n",Kpc);
        for (int i=1;i<=K;i+=2){
            long long tmp = (i-1)*Kpc + i + 1;
            if (tmp > lenK) tmp = lenK;
            anslist.push_back(tmp);
            //printf ("%I64d\n",tmp);
        }
    }else{
        for (int i=1;i<=K;i++){
            anslist.push_back(i);
        }
    }
    if (anslist.size()>S){
        printf ("IMPOSSIBLE\n");
        return;
    }else{
        for (int i=0;i<anslist.size();i++)
            printf ("%I64d ",anslist[i]);
        printf ("\n");
        return;
    }
}

int main(){
    freopen ("D-small-attempt0.in","r",stdin);
    freopen ("Dsmall.out","w",stdout);
    int TC;
    scanf ("%d",&TC);
    for (int tc=1;tc<=TC;tc++){
        printf ("Case #%d: ",tc);
        solve();
    }
return 0;
}
