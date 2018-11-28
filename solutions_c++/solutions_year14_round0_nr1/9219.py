#include <iostream>

using namespace std;

int main(void) {

    int tasks;
    int arr_ans1, arr_ans2, tmp, ans_count, ans;
    int arr_1[4], arr_2[4];

    cin >> tasks;
    for(int i = 0; i < tasks; i++) {

        ans_count = 0;

        /* get input */
        cin >> arr_ans1;
        for(int j = 1; j <= 4; j++) {
            for(int k = 0; k < 4; k++) {
                if(j == arr_ans1) {
                    cin >> arr_1[k];
                }
                else {
                    cin >> tmp;
                }
            }

        }
        cin >> arr_ans2;
        for(int j = 1; j <= 4; j++) {
            for(int k = 0; k < 4; k++) {
                if(j == arr_ans2) {
                    cin >> arr_2[k];
                }
                else {
                    cin >> tmp;
                }
            }
        }

        /* do match */
        for(int j = 0; j < 4; j++) {
            for(int k = 0; k < 4; k++) {
                if(arr_1[j] == arr_2[k]) {
                    ans = arr_1[j];
                    ans_count++;
                }
            }
        }

        if(ans_count == 0) {
            cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
        }
        else if(ans_count == 1) {
            cout << "Case #" << i+1 << ": " << ans << endl;
        }
        else {
            cout << "Case #" << i+1 << ": Bad magician!" << endl;
        }

    }

    return 0;

}
