#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outAlarge.txt", "w", stdout);

    int T = 0;
    cin >> T;
    for (int t = 1; t <= T; t++){
        priority_queue< pair<int,char> > party;
        int n = 0;
        cin >> n;
        int c = 'A';
        int counter = 0;
        for (int i = 0; i < n; i++){
            int x = 0;
            cin >> x;
            counter += x;
            party.push(make_pair(x,c));
            c++;
        }

        cout << "Case #" << t << ":";
        while (counter > 0){

            pair<int,char> a = party.top();
            party.pop();
            pair<int,char> b = party.top();
            party.pop();

            if (counter > 3 || counter == 2){
                if (a.first == b.first){
                    cout << " " << a.second << b.second;
                    a.first -= 1;
                    b.first -= 1;
                }
                else if (a.first > b.first){
                    cout << " " << a.second << a.second;
                    a.first -= 2;
                }
                else{
                    cout << " " << b.second << b.second;
                    b.first -= 2;
                }
                party.push(a);
                party.push(b);
                counter -= 2;
            }
            else{  // 1 oder 3
                cout << " " << a.second;
                counter -= 1;
                a.first -= 1;
                party.push(a);
                party.push(b);
            }
        }
        cout << endl;

    }




    return 0;
}
