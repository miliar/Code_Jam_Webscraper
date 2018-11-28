#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<list>
#include<math.h>
#include<algorithm>
#include<string>
#include<set>
#include<queue>
#include<fstream>
#define limit 1048576
#define inf 9223372036854775807ll
#define iinf 2147483647
#define mp make_pair
#define pb push_back
using namespace std;
int X[20];
int main(){
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A.out", "w",stdout);
    int t,r1,r2,tim=0,temp,cnt,ans;
    cin >> t;
    for(int i=0;i<t;i++){
            tim++;
            cnt=0;
            for(int j=1;j<=16;j++) X[j]=0;
            cin >> r1;
            for(int j=0;j<16;j++){
                cin >> temp;
                if (j/4+1==r1) X[temp]++;
            }
            cin >> r2;
            for(int j=0;j<16;j++){
                cin >> temp;
                if(j/4+1==r2) X[temp]++;
            }
            for(int j=1;j<=16;j++) if(X[j]==2){
                cnt++;
                ans=j;
            }
            if(cnt==0) cout << "Case #" <<tim<<": Volunteer cheated!\n";
            if(cnt==1) cout << "Case #"<<tim<<": "<<ans<<"\n";
            if(cnt>1) cout << "Case #"<<tim<<": Bad magician!\n";
    }
    return 0;
}
