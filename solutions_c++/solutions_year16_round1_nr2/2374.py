#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 50+1;
const int MAXM = 100+1;

int N,M;
int a[MAXN][MAXM];
int A[MAXN][MAXN];
int r[MAXN],c[MAXN];
bool flag;
int ans[MAXN];

void search(int d) {
    if (d==M) {
        /*for (int i = 0; i<N; ++i)
            if (r[i]!=-1) {
                bool valid = true;
                for (int k = 0; k<N; ++k)
                    if (A[i][k]!=a[r[i]][k])
                        valid = false;
                if (!valid) printf("aha\n");
            }
        for (int i = 0; i<N; ++i)
            if (c[i]!=-1) {
                bool valid = true;
                for (int k = 0; k<N; ++k)
                    if (A[k][i]!=a[c[i]][k])
                        valid = false;
                if (!valid) printf("aha\n");
            }*/
    
        int k = -1;
        for (int i = 0; i<N; ++i)
            if (r[i]==-1) k = i;
        if (k!=-1) {
            for (int i = 0; i<N; ++i)
                ans[i] = A[k][i];
            flag = 1;
            return;
        }
        for (int i = 0; i<N; ++i)
            if (c[i]==-1) k = i;
        if (k!=-1) {
            for (int i = 0; i<N; ++i)
                ans[i] = A[i][k];
            flag = 1;
            return;
        }
    }

    /*printf("depth=%d\n",d);
    for (int i = 0; i<N; ++i) {
        for (int j = 0; j<N; ++j)
            printf("%d ",A[i][j]);
        printf("\n");
    }*/
    
    bool rec[MAXN];
    memset(rec,0,sizeof(rec));
    //column
    for (int i = 0; i<N; ++i) {
        if ((A[0][i]==a[d][0] || A[0][i]==0) && c[i]==-1) {
            bool valid = true;
            for (int j = 0; j<N; ++j)
                if (A[j][i]!=0 && A[j][i]!=a[d][j]) valid = false;
            if (valid) {
                for (int j = 0; j<N; ++j)
                    if (A[j][i]==0) {
                        A[j][i] = a[d][j];
                        rec[j] = 1;
                    }
                c[i] = d;
                //printf("column %d = %d\n",i,d);
                search(d+1);
                if (flag) return;
                c[i] = -1;
                
                for (int j = 0; j<N; ++j)
                    if (rec[j]) {
                        A[j][i] = 0;
                        rec[j] = 0;
                    }
            }

        }
    }
    //row
    for (int i = 0; i<N; ++i) {
        if ((A[i][0]==a[d][0] || A[i][0]==0) && r[i]==-1) {
            bool valid = true;
            for (int j = 0; j<N; ++j)
                if (A[i][j]!=0 && A[i][j]!=a[d][j]) valid = false;
            if (valid) {
                for (int j = 0; j<N; ++j)
                    if (A[i][j]==0) {
                        A[i][j] = a[d][j];
                        rec[j] = 1;
                    }
                r[i] = d;
                //printf("row %d = %d\n",i,d);
                search(d+1);
                if (flag) return;
                r[i] = -1;
                
                for (int j = 0; j<N; ++j)
                    if (rec[j]) {
                        A[i][j] = 0;
                        rec[j] = 0;
                    }
            }
        }
    }
}

int main() {
    int T;
    cin>>T;
    for (int loop = 1; loop<=T; ++loop) {
        printf("Case #%d:",loop);
        cin>>N;
        M = 2*N-1;
        for (int i = 0; i<M; ++i) {
            for (int j = 0; j<N; ++j)
                cin>>a[i][j];
        }
        for (int i = 0; i<M; ++i)
            for (int j = i+1; j<M; ++j) {
                bool small = true;
                for (int k = 0; k<N; ++k)
                    if (a[i][k]>a[j][k]) small = false;
                    else if (a[i][k]<a[j][k]) break;
                if (!small) {
                    for (int k = 0; k<N; ++k)
                        swap(a[i][k],a[j][k]);
                }
            }
        memset(A,0,sizeof(A));
        for (int i = 0; i<N; ++i)
            A[0][i] = a[0][i];
        memset(r,-1,sizeof(r));
        memset(c,-1,sizeof(c));
        r[0] = 0;
        flag = false;
        search(1);
        for (int i = 0; i<N; ++i)
            printf(" %d",ans[i]); printf("\n");
    }
    return 0;
}