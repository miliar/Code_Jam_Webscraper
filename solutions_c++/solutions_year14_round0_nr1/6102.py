#include<iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<set>

using namespace std;

int main(){
    freopen("A-small.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    int a, aux;

    cin>>T;
    for(int i=1; i<=T; i++){
        set<int> cards;
        vector<int> ans;
        cin>>a;
        for(int j=1; j<=4; j++){
            for(int ii=0; ii<4; ii++){
                cin>>aux;
                if(j==a)
                    cards.insert(aux);
            }
        }

        cin>>a;
        for(int j=1; j<=4; j++){
            for(int ii=0; ii<4; ii++){
                cin>>aux;
                if(j==a){
                    if(cards.find(aux)!=cards.end())
                        ans.push_back(aux);
                }

            }
        }

        printf("Case #%d: ", i);
        if(ans.empty())
            printf("Volunteer cheated!\n");
        else if(ans.size()==1)
            printf("%d\n", ans[0]);
        else
            printf("Bad magician!\n");

    }


}
