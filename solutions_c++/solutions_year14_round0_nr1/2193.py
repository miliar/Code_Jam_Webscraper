#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.out", "w", stdout);
    int t; cin >> t;
    for(int te=1; te<=t; ++te){
        vector<int> v1, v2;
        int r1, r2, in;

        cin >> r1;
        for(int i=1; i<=4; ++i){
            for(int j=1; j<=4; ++j){
                cin >> in;
                if(i==r1)v1.push_back(in);
            }
        }
        cin >> r2;
        for(int i=1; i<=4; ++i){
            for(int j=1; j<=4; ++j){
                cin >> in;
                if(i==r2)v2.push_back(in);
            }
        }

        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());

        int cnt=0; int num;
        int i=0, j=0;
        while(i<v1.size() && j<v2.size()){
            if(v1[i]<v2[j])i++;
            else if(v1[i]>v2[j])j++;
            else{num=v1[i]; i++; j++; cnt++;}
        }

        if(cnt==1)printf("Case #%d: %d\n", te, num);
        else if(!cnt)printf("Case #%d: Volunteer cheated!\n", te);
        else if(cnt>1)printf("Case #%d: Bad magician!\n", te);
    }
    return 0;
}
