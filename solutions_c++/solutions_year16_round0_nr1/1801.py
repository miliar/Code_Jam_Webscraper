#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char **argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0), cout.precision(15);

    //1 100
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; cas ++){
        //0 1e6
        int N;
        cin >> N;
        if(N == 0){
            cout << "Case #" << cas << ": " << "INSOMNIA" << endl;
            continue;
        }
        vector<bool> d(10, false);
        //<=10
        int cnt = 0;
        for(int j = 1; j < 100; j++){
            //x < 1e6*100 = 1e8. in fact,  j <= 72.
            //at least effective (?*ABCD0*) lowest 4 digits will generate all 
            //digits in at most 72 steps (here only the last digit D must != 0)
            int x = j*N;
            while(x){
                int r = x%10;
                if(d[r] == false){
                    d[r] = true;
                    cnt ++;
                }
                x /= 10;
            }
            if(cnt == 10){
                cout << "Case #" << cas << ": " << j*N << endl;
                break;
            }
        }
    }

    return 0;
}
