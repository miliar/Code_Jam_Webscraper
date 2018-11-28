#include <iostream>

using namespace std;

class NewLotteryGame{
private:
    unsigned int count;
    unsigned int A, B, K, T;

public:
    NewLotteryGame(){
        A = B = K = T = 0;
    }

    void run(){
        cin >> T;

        for(unsigned int i = 0; i < T; i++){
            cin >> A >> B >> K;
            cout << "Case #" << i+1 << ": ";
            solve();
        }
    }

    void solve(){
        count = 0;
        for(unsigned int x = 0; x < A; x++)
            for(unsigned int y = 0; y < B; y++)
                if((x&y) < K){
                    //cout << "x " << x << " y " << y << endl;
                    count ++;
                }
        cout << count << endl;
    }
};


int main()
{
    NewLotteryGame *a = new NewLotteryGame();

    a->run();

    delete a;

    return 0;
}
