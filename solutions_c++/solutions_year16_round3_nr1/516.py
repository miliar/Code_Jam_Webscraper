#include <stdio.h>
#include <queue>
#include <algorithm>
#include <vector>
#define pii pair<int,int>
#define F first
#define S second
using namespace std;
priority_queue<pii> heap;
int a[26];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    int sm;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        int n;
        scanf("%d",&n);
        sm=0;
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
            sm+=a[i];
        }
        for(int i=0;i<n;i++){
            heap.push(pii(a[i],i));
        }
        printf("Case #%d: ",t);
        while(!heap.empty()){
            pii x=heap.top();
            heap.pop();
            x.F--;
            printf("%c",x.S+'A');
            if(x.F!=0){
                heap.push(x);
            }
            if(heap.empty()||sm%2==1){
                sm=0;
                printf(" ");
                continue;
            }
            x=heap.top();
            heap.pop();
            x.F--;
            printf("%c",x.S+'A');
            if(x.F!=0){
                heap.push(x);
            }
            if(!heap.empty())   printf(" ");
        }
        printf("\n");
    }
}
