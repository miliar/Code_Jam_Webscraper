#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
using namespace std;
int s[100005],bit;
vector<pair<int,int> > arr;
int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,m,i,j,ans,C=0,l,r;
    scanf("%d",&t);
    while(t--){
        int val=0,id;
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%d",&s[i]);
        }
        l=0,r=n-1;
        int tmp=0;
        while(l<r){
            int val=-1,id;
            for(i=l;i<=r;i++){
                if(val==-1 || s[i]<val){
                    val=s[i],id=i;
                }
            }
            //printf("%d..%d..%d..\n",val,id,r);
            if(id-l<r-id){
                for(j=id-1;j>=l;j--){
                    swap(s[j],s[j+1]);
                    tmp++;
                }
                l++;
            }
            else{
                for(j=id;j<r;j++){
                    swap(s[j],s[j+1]);
                    tmp++;
                }
                r--;
            }
        }
        printf("Case #%d: %d\n",++C,tmp);
    }
}
