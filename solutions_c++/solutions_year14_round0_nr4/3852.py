//dayka
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    ios_base::sync_with_stdio(0);

    int i,
        t, nt,
        blocks_number,
        new_result, old_result,
        ken_pos, naomi_pos,
        counter;
    double da;

    vector<double> naomi;
    vector<double> ken;

    cin >> t;

    for(nt=1 ; nt<=t ; nt++)
    {
        new_result = 0;
        old_result = 0;
        naomi_pos = 0;
        ken_pos = 0;
        cin >> blocks_number;
        for(i=0 ; i<blocks_number ; i++)
        {
            cin >> da;
            naomi.push_back(da);
        }
        for(i=0 ; i<blocks_number ; i++)
        {
            cin >> da;
            ken.push_back(da);
        }
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        for(i=0 ; i<naomi.size() ; i++)
        {
            if(ken_pos >= ken.size());
            else if(naomi[i] > ken[ken_pos])
            {
                ken_pos++;
                i--;
            }
            else
            {
                new_result++;
                ken_pos++;
            }
        }
        new_result = naomi.size() - new_result;
        for(i=0 ; i<ken.size() ; i++)
        {
            if(naomi_pos>=naomi.size());
            else if(ken[i] > naomi[naomi_pos])
            {
                naomi_pos++;
                i--;
            }
            else
            {
                old_result++;
                naomi_pos++;
            }
        }

        cout << "Case #" << nt << ": " << old_result << " " << new_result << endl;
        naomi.clear();
        ken.clear();
    }

return 0;
}
