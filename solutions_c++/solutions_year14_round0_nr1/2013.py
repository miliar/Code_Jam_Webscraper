#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <string.h>
using namespace std;
int main(){
    freopen("a.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int uu=0;uu<t;uu++){
        int a;
        int b[4][4];
        scanf("%d",&a);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d ",&b[i][j]);
            }
        }
        map<int,int> mp;
        mp[b[a-1][0]]=1;
        mp[b[a-1][1]]=1;
        mp[b[a-1][2]]=1;
        mp[b[a-1][3]]=1;
        scanf("%d",&a);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d ",&b[i][j]);
            }
        }
        int ct = 0;
        int ans;
        if(mp[b[a-1][0]]){
            ct++;
            ans=b[a-1][0];
        }
        if(mp[b[a-1][1]]){
            ct++;
            ans=b[a-1][1];
        }
        if(mp[b[a-1][2]]){
            ct++;
            ans=b[a-1][2];
        }
        if(mp[b[a-1][3]]){
            ct++;
            ans=b[a-1][3];
        }
        printf("Case #%d: ",uu+1);
        if(ct==0) printf("Volunteer cheated!\n");
        if(ct>1) printf("Bad magician!\n");
        if(ct==1) printf("%d\n",ans);
    }
    return 0;
}
