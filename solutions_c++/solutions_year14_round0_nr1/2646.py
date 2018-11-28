#include <cstdio>
#include <vector>

using namespace std;

vector<int> getVolunteerRow() {
    int row;
    scanf("%d", &row);
    vector<int> resultRow;

    for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 4; ++j) {
            int card;
            scanf(" %d", &card);
            if(i + 1 == row) {
                resultRow.push_back(card);
            }
        }
    }
    return resultRow;
}

vector<int> findCommon(vector<int> cardMatrix1, vector<int> cardMatrix2) {
    vector<int> common;
    for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 4; ++j) {
            if(cardMatrix1[i] == cardMatrix2[j]) {
                common.push_back(cardMatrix1[i]);
            }
        }
    }
    return common;
}

int main() {
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) { 
        vector<int> firstAns = getVolunteerRow();
        vector<int> secondAns = getVolunteerRow();

        vector<int> commonCard = findCommon(firstAns, secondAns);

        printf("Case #%d: ", t);
        if(commonCard.empty()) {
            printf("Volunteer cheated!");
        } else if(commonCard.size() > 1) {
            printf("Bad magician!");
        } else {
            printf("%d", commonCard[0]);
        }
        printf("\n");

    }

    return 0;
}
