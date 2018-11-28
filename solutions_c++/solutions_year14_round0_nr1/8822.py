#include <stdio.h>
#include <set>
#include <vector>
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt", "w", stdout);
    int nTest, cards[4], iCurrentTest, iAnswer, iRow, iColumn;
    std::set<int> setCards1, setCards2;
    scanf("%d", &nTest);
    for (iCurrentTest = 1; iCurrentTest <= nTest; iCurrentTest++)
    {
        scanf("%d", &iAnswer);
        for (iRow = 1; iRow <= 4; iRow++)
        {
            for (iColumn = 0; iColumn < 4; iColumn++)
            {
                scanf("%d", &cards[iColumn]);
            }
            if (iRow == iAnswer)
            {
                setCards1 = std::set<int>(cards, cards + 4);
            }
        }
        scanf("%d", &iAnswer);
        for (iRow = 1; iRow <= 4; iRow++)
        {
            for (iColumn = 0; iColumn < 4; iColumn++)
            {
                scanf("%d", &cards[iColumn]);
            }
            if (iRow == iAnswer)
            {
                setCards2 = std::set<int>(cards, cards + 4);
            }
        }
        std::vector<int> vecAnswers;
        for (std::set<int>::iterator it = setCards1.begin(); it != setCards1.end(); it++)
        {
            if (setCards2.count(*it) > 0)
            {
                vecAnswers.push_back(*it);
            }
        }
        int nSize = static_cast<int>(vecAnswers.size());
        printf("Case #%d: ", iCurrentTest);
        if (nSize == 0)
        {
            printf("Volunteer cheated!\n");
        }
        else if (nSize > 1)
        {
            printf("Bad magician!\n");
        }
        else
        {
            printf("%d\n", vecAnswers[0]);
        }
    }
    return 0;
}