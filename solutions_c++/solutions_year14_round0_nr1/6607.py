#include<iostream>
#include<string.h>
#include<stdio.h>
#include<string>
#include<cmath>
#include<algorithm>
#include<set>

using namespace std;

#define in() ({ int x; scanf("%d", &x); x; })
#define fr(i,n) for(i = 0; i < n; i++)

void INPUT_FROM_FILE()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    #endif
}

int main()
{
    //INPUT_FROM_FILE();
    int T, ans1, ans2, i, j, answer;
    int arr[4][4];
    bool flag;
    set<int> set1;
    set<int> set2;
    set<int>::iterator it1;
    set<int>::iterator it2;
    cin >> T;
    for (i=0; i<T; i++) {
        answer = 0;
        flag = false;
        set1.clear();
        set2.clear();
        cin >> ans1;
        for (j=0; j<4; j++) {
            cin >> arr[j][0] >> arr[j][1] >> arr[j][2] >> arr[j][3];
        }
        set1.insert(arr[ans1-1][0]);
        set1.insert(arr[ans1-1][1]);
        set1.insert(arr[ans1-1][2]);
        set1.insert(arr[ans1-1][3]);

        cin >> ans2;
        for (j=0; j<4; j++) {
            cin >> arr[j][0] >> arr[j][1] >> arr[j][2] >> arr[j][3];
        }
        set2.insert(arr[ans2-1][0]);
        set2.insert(arr[ans2-1][1]);
        set2.insert(arr[ans2-1][2]);
        set2.insert(arr[ans2-1][3]);

        for (it1=set1.begin(); it1!=set1.end(); ++it1) {
            it2 = set2.find(*it1);
            if (it2 != set2.end() && answer == 0) {
                answer = *it1;
            } else if (it2 != set2.end() && answer > 0) {
                cout << "Case #" << i+1 << ": Bad magician!\n";
                flag = true;
                break;
            }
        }
        if (! flag) {
            if (answer > 0) {
                cout << "Case #" << i+1 << ": "<< answer << endl;
            } else {
                cout << "Case #" << i+1 << ": Volunteer cheated!\n";
            }
        }
    }
    return 0;
}
