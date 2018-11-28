#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int mat[200][200];
int mmax[200];
int id[200];
int mark[200];

int main(int argc, const char * argv[])
{
	freopen("B-small-attempt0.in","r",stdin);    freopen("B-large.out","w",stdout);

    int T,M,N;
    cin>>T;
    for(int ca=1;ca<=T;ca++){
        cin>>N>>M;
        for(int i=0;i<M;i++) mark[i]=0;
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                scanf("%d",&mat[i][j]);
                if(j==0) mmax[i]=mat[i][j];
                else mmax[i]=max(mmax[i],mat[i][j]);
            }
        }
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(mat[i][j]<mmax[i]) mark[j]=1;
            }
        }

        int flag=1;
        for(int i=0;i<M && flag;i++){
            if(mark[i]==0) continue;
            for(int j=1;j<N && flag;j++){
                if(mat[j][i]!=mat[j-1][i]) flag=0;
            }
        }
        if(flag==1) printf("Case #%d: YES\n",ca);
        else printf("Case #%d: NO\n",ca);
    }
    
    return 0;
}

