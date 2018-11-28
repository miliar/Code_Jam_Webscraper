#include<bits/stdc++.h>
using namespace std;
const int nmax=100000;

vector<int> e[nmax],q;
int n,u,v,s,t,ntest,mark[nmax],lab,r[nmax];
char a[100];

main(){
    //freopen("out.txt","w",stdout);
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;test++){
        scanf("%s",a);
        n=strlen(a);
        /*
        u=0;
        for (int i=0;i<n;i++) u+=(a[i]=='-')<<i;
        q.clear();
        q.push_back(u);
        mark[u]=++lab;
        r[u]=0;
        for (int i=0;i<q.size();i++){
            u=q[i];
            for (int j=1;j<=n;j++){
                v=((u>>j)<<j);
                for (int t=0;t<j;t++) v+=(1-((u>>t)&1))<<(j-t-1);
                if (mark[v]!=lab){
                    mark[v]=lab;
                    q.push_back(v);
                    r[v]=r[u]+1;
                }
            }
        }
        printf("Case #%d: %d\n",test,r[0]);
        */
        int last=n,res=0;
        while (last>0 && a[last-1]=='+') last--;
        while (last > 0){
            if (a[0]=='+'){
                int first=0;
                while (first<n-1 && a[first+1]=='+') {a[first++]='-';}
                a[first]='-';
                res++;
            }
            int first=0;
            while (first<n-1 && a[first+1]=='-') {a[first++]='+';}
            a[first]='+';
            res++;
            while (last>0 && a[last-1]=='+') last--;
        }
        printf("Case #%d: %d\n",test,res);
    }
}
