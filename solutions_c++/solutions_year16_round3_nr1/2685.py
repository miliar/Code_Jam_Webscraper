#include <iostream>
#include <queue>
#include <utility>
using namespace std;
int main(int argc, char **argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0), cout.precision(15);
    //1 50
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; cas ++){
        cout << "Case #" << cas << ":";
        //2 26
        int N;
        cin >> N;
        //num party
        priority_queue<pair<int, char> > q;
        //sum(Pi) <= 1e3
        int cnt = 0;
        for(int i = 0; i < N; i++){
            //Pi 1 1e3 sum <= 1e3
            int Pi;
            cin >> Pi;
            q.push(make_pair(Pi, i + 'A'));
            cnt += Pi;
        }
        pair<int, char> p;
        if(cnt%2){
            p = q.top();
            q.pop();
            cout << ' ' << p.second;
            p.first --;
            if(p.first > 0){
                q.push(p);
            }
            cnt--;
        }
        while(q.size()){
            pair<int, char> p = q.top();
            q.pop();
            cout << ' ' << p.second;
            p.first --;
            cnt --;
            if(p.first > 0){
                q.push(p);
            }
            if(q.empty()){
                cerr << "should not reach here" << endl;
                break;
            }
            p = q.top();
            q.pop();
            cout << p.second;
            p.first --;
            if(p.first > 0){
                q.push(p);
            }
            cnt --;
            if(q.size() && q.top().first > cnt/2){
                cerr << "fail " << endl;
            }
        }
        cout << endl;
        if(cnt != 0){
            cerr << "fail cnt" << " case " << cas << " cnt " << cnt << endl;
        }
    }
    return 0;
}
