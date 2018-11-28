#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int caseCount;

    scanf(" %d", &caseCount);
    for(int caseIndex = 1; caseIndex <= caseCount; caseIndex++) {
        int blockCount, deceitfulPoint = 0, warPoint = 0;;
        vector<float> naomi;
        vector<float> ken;

        scanf(" %d", &blockCount);
        for(int i = 0; i < blockCount; i++) {
            float tmp;
            scanf(" %f", &tmp);
            naomi.push_back(tmp);
        }
        for(int i = 0; i < blockCount; i++) {
            float tmp;
            scanf(" %f", &tmp);
            ken.push_back(tmp);
        }

        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        reverse(naomi.begin(), naomi.end());
        reverse(ken.begin(), ken.end());

        /*
        for(int i = 0; i < blockCount; i++) {
            printf("%f ", naomi[i]);
        }
        printf("\n");
        for(int i = 0; i < blockCount; i++) {
            printf("%f ", ken[i]);
        }
        printf("\n");
        */

        vector<float> tmpNaomi = naomi;
        vector<float> tmpKen= ken;

        // Calculate deceitful Point
        for(int i = blockCount - 1; i >= 0; i--) {
            if(naomi[i] < ken.back()) {
                ken.erase(ken.begin());
            }
            else {
                deceitfulPoint++;
                ken.pop_back();
            }
        }

        naomi = tmpNaomi;
        ken = tmpKen;
        
        // Calculate war Point
        for(int i = 0; i < blockCount; i++) {
            if(naomi[i] > ken[0]) {
                warPoint++;
                ken.pop_back();
            }
            else {
                ken.erase(ken.begin());
            }
        }

        printf("Case #%d: %d %d\n", caseIndex, deceitfulPoint, warPoint);
    }

    return 0;
}
