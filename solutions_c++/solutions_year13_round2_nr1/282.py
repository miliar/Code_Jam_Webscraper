#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<set>
#include<vector>
using namespace std;
#define inf 1000001

int OPT[1010000];
int OPT2[1010000];
int A,N;
pair<int,int> st[1010000];
int front=0,rear=0;
void solve(){
    scanf("%d %d",&A,&N);
    for(int i=0;i<=1000001;i++)OPT[i]=OPT2[i]=inf;
    OPT[A]=0;
    vector<int> v;
    for(int i=0;i<N;i++){
        int k;
        scanf("%d",&k);
        v.push_back(k);
    }
    sort(v.begin(),v.end());
    for(int i=0;i<N;i++){
        int k=v[i];
        //for(int j=0;j<=1000001;j++)OPT2[j]=min(inf,OPT[j]+1);
        front=0;rear=0;
        for(int j=3;j<=1000001;j++){
            st[rear]=make_pair(OPT[j-1],j-1);
            while(rear>front&&st[rear].first<=st[rear-1].first){
                swap(st[rear],st[rear-1]);
                --rear;
            }
            rear++;
            while(front<rear&&st[front].second*2<=j)front++;
            if(front<rear){
                //if(j<=30)printf("%d %d %d\n",j,st[front].first,st[front].second);
                OPT[j]=min(OPT[j],OPT[st[front].second]+1);
            }

        }
        for(int j=0;j<=1000001;j++)OPT2[j]=min(inf,OPT[j]+1);
        for(int j=k+1;j<=1000001;j++){
            OPT2[min(inf,j+k)]=min(OPT2[min(inf,j+k)],OPT[j]);
        }
        for(int j=0;j<=1000001;j++)OPT[j]=OPT2[j];
        /*for(int j=0;j<=30;j++){
            if(OPT[j]==inf)printf("oo ");
            else printf("%d ",OPT[j]);

        }
        printf("\n");*/
    }
    int k=inf;
    for(int i=0;i<=1000001;i++)k=min(OPT[i],k);
    printf("%d\n",k);
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
