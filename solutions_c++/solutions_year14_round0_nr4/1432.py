#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

int main()
{
    int num_cases;

    cin >> num_cases;
    for(int case_num = 1; case_num <= num_cases; ++case_num) {
        int num_blocks;
        cin >> num_blocks;

        deque<double> naomi(num_blocks);
        deque<double> ken(num_blocks);

        for(int i = 0; i < num_blocks; ++i)
            cin >> naomi[i];
        for(int i = 0; i < num_blocks; ++i)
            cin >> ken[i];
       
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());

        int i, j;
        for(i = 0, j = 0; i < num_blocks && j < num_blocks; ++i, ++j) {
            while(j < num_blocks && ken[j] < naomi[i])
                j++;
            if(j >= num_blocks)
                break;
        }

        int good_score = j - i;

        sort(ken.rbegin(), ken.rend());
        int evil_score = 0;

        while(num_blocks --> 0) {
            if(naomi.front() < ken.front() && naomi.front() < ken.back()) {
                naomi.pop_front();
                ken.pop_front();
            } else if(naomi.front() > ken.front()) {
                naomi.pop_front();
                ken.pop_front();
                evil_score++;
            } else {
                naomi.pop_front();
                ken.pop_back();
                evil_score++;
            }
        }

        cout << "case #" << case_num << ": " << evil_score << " " << good_score << endl;
    }

    return 0;
}