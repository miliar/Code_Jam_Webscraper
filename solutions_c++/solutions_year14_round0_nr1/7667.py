#include <iostream>
#include <set>
#include <cstdio>
using namespace std;
#define FROM_FILE
#define SMALL_INPUT_FNAME "A-small-attempt0.in"
#define OUTPUT_FNAME "big_output.txt"
const static int NUM = 4;

int main()
{
    #ifdef FROM_FILE
        freopen(SMALL_INPUT_FNAME, "r", stdin);
        freopen(OUTPUT_FNAME, "w", stdout);
    #endif // FROM_FILE

    int caseNum;
    scanf("%d", &caseNum);
    for (int T = 1; T <= caseNum; ++T) {
        int frow = 0, srow = 0;
        scanf("%d", &frow);
        set<int> frow_elem;
        for (int i = 1; i <= NUM; ++i) {
            for (int j = 1; j <= NUM; ++j) {
                int candi_num;
                scanf("%d", &candi_num);
                if (i == frow) {
                    frow_elem.insert(candi_num);
                }
            }
        }
        set<int> common_elems;
        scanf("%d", &srow);
        for (int i = 1; i <= NUM; i++) {
           for (int j = 1; j <= NUM; ++j) {
                int candi_num;
                scanf("%d", &candi_num);
                if (i == srow && frow_elem.find(candi_num) != frow_elem.end()) {
                    common_elems.insert(candi_num);
                }
            }
        }
        printf("Case #%d: ", T);
        if (common_elems.size() == 0) {
            printf("Volunteer cheated!\n");
        }
        else if (common_elems.size() == 1) {
            printf("%d\n", *common_elems.begin());
        }
        else {
            printf("Bad magician!\n");
        }
    }
    return 0;
}
