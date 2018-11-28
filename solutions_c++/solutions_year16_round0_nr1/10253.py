#include <iostream>
using namespace std;

int main() {
    int caseNum;

    scanf("%d", &caseNum);
    for (int caseCount=1; caseCount<=caseNum; caseCount++) {
        int inNum;

        scanf("%d", &inNum);
        printf("Case #%d: ", caseCount);
        if (inNum == 0) { printf("INSOMNIA\n"); }
        else {
            int nowNum;
            const int TABLE_SIZE = 10;
            bool table[TABLE_SIZE] = {};

            for (int i=1;; i++) {
                bool isOver = true;

                nowNum = inNum * i;
                for (int j=nowNum; j!=0; j/=10) { table[j%10] = true; }
                for (int j=0; j<TABLE_SIZE; j++) {
                    if (!table[j]) {
                        isOver = false;
                        break;
                    }
                }
                if (isOver) { break; }
            }
            printf("%d\n", nowNum);
        }
    }

    return 0;
}
