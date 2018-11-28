#include <iostream>
#include <vector>
using namespace std;
int A[2000], B[2000];
int last[3000];
bool edge[2000][2000];
vector<int> edges[2000];
int themin[2000];
void addedge(int a, int b) {
    edge[a][b] = true;
    edges[b].push_back(a);
//    printf("%d to %d\n",b,a);
}
bool isp[2000];
void go(int cur) {
    if (isp[cur]) return;
    isp[cur] = true;
    for (vector<int>::iterator it = edges[cur].begin(); it!=edges[cur].end(); it++) {
        go(*it);
    }
}
int main() {
    int T; scanf("%d",&T); for (int t=1; t<=T; t++) {
        int N; scanf("%d",&N);
        
        memset(edge,0,2000*2000);
        for (int i=0; i<2000; i++) edges[i].clear();
        
        for (int i=0; i<N; i++) scanf("%d",&A[i]);
        for (int i=0; i<N; i++) scanf("%d",&B[i]);        

        memset(last,-1,3000*sizeof(int));
                
        for (int i=0; i<N; i++) {
            if (last[A[i]]>=0) {
                addedge(i,last[A[i]]);
            }
            if (last[A[i]-1]>=0) {
                addedge(last[A[i]-1],i);
            }
            last[A[i]]=i;
            // must be less than the previous A[i]
            // must be greaterthan the previous A[i]-1
        }
        // reverse for B
        memset(last,-1,3000*sizeof(int));
                
        for (int i=N-1; i>=0; i--) {
            if (last[B[i]]>=0) {
                addedge(i,last[B[i]]);
            }
            if (last[B[i]-1]>=0) {
                addedge(last[B[i]-1],i);
            }
            last[B[i]]=i;
        }
        
        printf("Case #%d: ",t);
        
        for (int i=0; i<N; i++) themin[i] = 0;
        
        for (int i=0; i<N; i++) {
            // find all parents
            // find all nonparents
//            printf("i = %d\n",i);
            
            for (int j=0; j<N; j++) isp[j] = false;
            
            go(i);
            
            int ct = themin[i];
            for (int j=0; j<N; j++) if (isp[j]) ct++;           
            printf("%d ",ct);
            
            for (int j=0; j<N; j++) if (!isp[j] && themin[j]==themin[i]) {
                themin[j]>?=ct;
//                printf("themin[%d] = %d\n",j,ct);
            }
            
            for (int j=0; j<N; j++) if (!isp[j])
            for (vector<int>::iterator it = edges[j].begin(); it!=edges[j].end();) {
                if (isp[*it]) {
//                    printf("Erase %d -> %d\n",j,*it);  
                    it = edges[j].erase(it);
                } else it++;
            }            
        }
        printf("\n");
        
    }
}
