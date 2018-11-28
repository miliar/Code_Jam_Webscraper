//HARE KRISHNA
#include<bits/stdc++.h>
using namespace std;

#define pb push_back
int howm[30];
int main(){
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,tcase;
    int n;
    scanf("%d",&t);
    for(tcase=1;tcase<=t;tcase++){
        memset(howm,0,sizeof(howm));
        scanf("%d",&n);
        int i,tmp;
        int total=0;
        for(i=1;i<=n;i++){
            scanf("%d",&tmp);
            howm[i-1]+=tmp;
            total+=tmp;
        }
        vector<string>ans;
        vector<int>hu;
        int cntano=0;
        int j;
        while(1){
            if(total<=0)break;
            hu.clear();
            cntano=0;
            int pro=(total-2)/2;
            int so=pro+1;
            for(i=0;i<=25;i++){
                if(howm[i]>pro){
                    int cntw=(howm[i]-pro);
                    for(j=0;j<cntw;j++){
                        hu.pb(i);
                    }
                    howm[i]-=cntw;
                    cntano+=cntw;
                }
            }
            if(cntano<=2){
                int rem=2-cntano;
                for(j=0;j<rem;j++){
                    int maxx=-1;
                    int ind;
                    for(i=0;i<=25;i++){
                        if(maxx<howm[i]){
                            maxx=howm[i];
                            ind=i;
                        }
                    }
                    howm[ind]--;
                    hu.pb(ind);
                }
                cntano=2;
            }
            int sz=hu.size();
            if(sz<=2){
                string ano="";
                ano+=('A'+hu[0]);
                ano+=('A'+hu[1]);
                ans.pb(ano);
            }
            else{
                string ano="";
                ano+=('A'+hu[0]);
                ans.pb(ano);
                ano="";
                ano+=('A'+hu[1]);
                ano+=('A'+hu[2]);
                ans.pb(ano);
            }
            total=total-cntano;

        }
        printf("Case #%d: ",tcase);

        int szano=ans.size();
        cout<<ans[0];
        for(i=1;i<szano;i++){
            cout<<" "<<ans[i];
        }
        cout<<endl;
    }
    return 0;
}
