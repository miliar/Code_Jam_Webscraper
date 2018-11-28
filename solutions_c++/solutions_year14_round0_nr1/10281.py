#include <iostream>
#include <fstream>
#include <map>
using namespace std;

int t;
int cards[4][4];

int main()
{
    ifstream cin("magic.in");
    ofstream cout("magic.out");
    cin >> t;
    for(int k(1); k <= t; k++) {
        int a;
        cin >> a;
        a--;
        for(int i(0); i < 4; i++) {
            for(int j(0); j < 4; j++) {
                cin >> cards[i][j];
            }
        }
        map<int, int> selectedCards;
        map<int, int>::iterator it;
        for(int i(0); i < 4; i++) {
            selectedCards[cards[a][i]]++;
        }
        cin >> a;
        a--;
        for(int i(0); i < 4; i++) {
            for(int j(0); j < 4; j++) {
                cin >> cards[i][j];
            }
        }
        for(int i(0); i < 4; i++) {
            selectedCards[cards[a][i]]++;
        }
        int totalCards = 0;
        int card;
        for(it = selectedCards.begin(); it != selectedCards.end(); it++) {
            if(it->second == 2) {
                totalCards++;
                card = it->first;
            }
        }
        cout << "Case #" << k << ": ";
        if(totalCards == 0) cout << "Volunteer cheated!\n";
        else if(totalCards == 1) cout << card << "\n";
        else cout << "Bad magician!\n";
    }
    return 0;
}
