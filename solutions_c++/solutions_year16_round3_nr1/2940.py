#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>


using namespace std;

int main(int argc, char **argv) {
    int T;
    cin >> T;

    for(int k = 0; k < T; k++){
        int N;
        cin >> N;

        priority_queue<pair<int, char>> salle;
        int sum = 0;

        for(int n = 0; n < N; n++){
            int p;
            cin >> p;
            salle.push(pair<int, char>(p, 'A' + n));
            sum += p;
        }

        cout << "Case #" << to_string(k + 1) << ": ";

//        for(int n = 0; n < N; n++){
//            cout << salle.top().first << " " << salle.top().second << endl;
//            salle.pop();
//        }

        int counter = 0;

        while(!salle.empty() && counter < 10){

            pair<int, char> first = salle.top();
            salle.pop();
            pair<int, char> second = salle.top();
            salle.pop();

//            cout << first.first << " " << first.second << "/" << second.first << " " << second.second << "/" << sum << endl;

            if(first.first == 1){
                if(sum % 2 == 1){
                    first.first -= 1;
                    sum -=1;

                    cout << first.second << " ";
                }
                else {
                    first.first -= 1;
                    second.first -= 1;
                    sum -= 2;

                    cout << first.second << second.second << " ";
                }
            }
            else {
                if (first.first == second.first) {
                    first.first -= 1;
                    second.first -= 1;
                    sum -= 2;

                    cout << first.second << second.second << " ";
                }
                else if (first.first > second.first) {
                    first.first -= 2;
                    sum -= 2;

                    cout << first.second << first.second << " ";
                }
                else if (first.first < second.first) {
                    second.first -= 2;
                    sum -= 2;

                    cout << second.second << second.second << " ";
                }
            }

            counter++;

            if(first.first > 0)
                salle.push(first);
            if(second.first > 0)
                salle.push(second);
        }

        cout << endl;
    }

    return 0;
}

