#include <iostream>
#include <queue>
#include <vector>
#include <functional>
using namespace std;

typedef  pair<int, char> pic;


int main() {
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        string result;
        int left = 0;
    std::priority_queue<pic> h;
        int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        h.push(make_pair(x, 'A' + i));
    }

        left = n;

        while (1) {
            auto v1 = h.top();
            h.pop();


            if (v1.first == 0) {
                break;
            }

            result.push_back(v1.second);

            if (left == 2) {
                auto v2 = h.top();
                h.pop();
                result.push_back(v2.second);
                v2.first--;
                if (v2.first == 0) {
                    --left;
                }
                    h.push(v2);

            }

            v1.first--;
            if (v1.first == 0) {
                --left;
            }
            h.push(v1);



            result += " ";
        }


        cout << "Case " << "#" << t << ": " << result << "\n";




    }
}
