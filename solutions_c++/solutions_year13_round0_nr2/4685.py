#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

const char* str[] = {"NO", "YES"};

int a[105][105];

int main(){
    int cs,no=0;
    scanf("%d",&cs);
    while(cs--){
        int n,m,ans=1,row[105]={},col[105]={};
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++) for(int j=0;j<m;j++){
            scanf("%d",&a[i][j]);
            row[i]=max(row[i],a[i][j]);
            col[j]=max(col[j],a[i][j]);
        }
        for(int i=0;i<n;i++) for(int j=0;j<m;j++)
            if(a[i][j]!=min(row[i],col[j])) ans=0;
        printf("Case #%d: %s\n",++no,str[ans]);
    }
}
