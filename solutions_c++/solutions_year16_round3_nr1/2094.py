#include <stdio.h>
#include <vector>
#include <queue>
#include <functional>

using namespace std;

int t, n;

class Party
{
public:
    char party;
    int count;
};

struct LessThanByCount
{
  bool operator()(const Party& lhs, const Party& rhs) const
  {
    return lhs.count < rhs.count;
  }
};

int main(int argc, char const *argv[]) {
    scanf("%d\n", &t);
    for(int i=0;i<t;i++){
        priority_queue<Party, vector<Party>, LessThanByCount> parties;
        scanf("%d\n", &n);
        for(int j=0;j<n;j++){
            Party party;
            party.party = 'A' + j;
            scanf("%d", &(party.count));
            parties.push(party);
        }
        scanf("\n");
        printf("Case #%d:", i+1);
        while(!parties.empty()){
            if(parties.size()==3 && parties.top().count==1){
                Party party1 = parties.top();
                parties.pop();
                printf(" %c", party1.party);
            }else{
                Party party1 = parties.top();
                parties.pop();
                Party party2 = parties.top();
                parties.pop();
                if(party1.count != party2.count){
                    printf(" %c%c", party1.party, party1.party);
                    party1.count-=2;
                    if(party1.count) parties.push(party1);
                    parties.push(party2);
                }else{
                    printf(" %c%c", party1.party, party2.party);
                    party1.count--;
                    party2.count--;
                    if(party1.count) parties.push(party1);
                    if(party2.count) parties.push(party2);
                }
            }
        }
        printf("\n");
    }
    return 0;
}
