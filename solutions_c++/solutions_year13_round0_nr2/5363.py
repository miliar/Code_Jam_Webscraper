#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdio>
using namespace std;
int n,m,a[101][101];
int scanrow(int i)
{
    int t=a[i][0];
    for(int j=0; j<m; j++)
        if(a[i][j]!=t) return 0;
    return 1;
}
int scancolumn(int j)
{
    int t=a[0][j];
    for(int i=0; i<n; i++)
        if(a[i][j]!=t) return 0;
    return 1;
}
int main()
{
    int t=0,k=0;
    freopen("B-small-attempt1.in","r",stdin);
    freopen("Bout","w",stdout);
    scanf("%d",&t);
    while(t--){
        k++;
        bool flag=1;
        scanf("%d %d",&n,&m);
        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
                scanf("%d",&a[i][j]);
        int maxa=a[0][0];
        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
                maxa=max(maxa,a[i][j]);
        int to[101][101];
        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
                to[i][j]=maxa;
        for(int i=0; i<n; i++)
            if(scanrow(i)==1) {
                int tem=a[i][0];
                for(int j=0; j<m; j++)
                    to[i][j]=tem;
            }
        for(int j=0; j<m; j++) {
            if(scancolumn(j)==1) {
                int tem=a[0][j];
                for(int i=0; i<n; i++)
                    to[i][j]=tem;
            }
        }

        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
                if(a[i][j]!=to[i][j]) {
                    flag=0;
                    break;
                }
        string result="YES";
        if(flag!=1)
            result="NO";
        cout<<"Case #"<<k<<": "<<result<<endl;
        //k++;
    }
    return 0;
}
