#include <iostream>
#include <vector>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    for(int i=0;i!=cases;i++){
        int parties;
        cin >> parties;
        vector<pair<int,int> > party(parties);
        for(int j=0;j!=parties;j++){
            int num;
            cin >> num;
            party[j] = pair<int,int>(j,num);
        }
        bool changed = true;
        while (changed) {
            changed = false;
            for (int j = 0; j != parties-1; j++) {
                    if (party[j].second > party[j+1].second) {
                        pair<int, int> temp = party[j+1];
                        party[j+1] = party[j];
                        party[j] = temp;
                        changed = true;
                    }
                }
        }
        string ans;
        while(party[party.size()-1].second){
            for(int j=0;j!=party.size();j++){
                if(party[j].second){
                    ans.push_back((char)(party[j].first+65));
                    party[j].second--;
                }
            }
        }
        cout << "Case #" << i+1 << ": " ;
        for(int j=ans.size()-1;j!=-1;j--){
            cout << ans[j];
            if(!(j%2))
                cout << " ";
        }
        cout <<endl;
    }
    return 0;
}