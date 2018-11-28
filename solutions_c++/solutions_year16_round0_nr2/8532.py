#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
const int MAXN = 105;
bool states[MAXN];
int T, N;
string line;

// 0 == don't flip anything yet
// -1 == flip whole stack
// else == flip top pancake
int nextMove(int bottom)
{
    //cout << states[0] << " " << states[bottom] << endl;
    if (states[bottom]){
        return -2;
    }else{
        // if the bottom one is -

        // if top is also '-' then flip whole stack from current bottom
        if (!states[0]){
            return -1;
        }
        // if top is + then find where the + end and flip those instead
        else{
            int top = 0;
            while (states[top])
            {
                top++;
            }
            //cout << "nextMove: flip from: " << top-1 << endl;
            return top-1;
        }
    }

}

void flip(int right)
{
    int left = 0, temp;
    while (! (left > right)){
        //cout << left << " " << right << endl;
        //cout << "in flip: " << states[left] << " " << states[right] << endl;
        //cout << "swapping: " << !states[left] << " " << !states[right] << endl;
        temp = !states[left];
        states[left] = !states[right];
        states[right] = temp;

        left++;
        right--;
    }
    //cout << "after flip: " << states[left] << " " << states[right] << endl;
}

void coutStates()
{
    for (int i = 0; i < N; i++){
        cout << states[i];
    }
    cout << endl;
}

int main()
{
    freopen("/Users/yan/Documents/Prep/codeJame/pancakeDATALarge.txt", "r", stdin);
    freopen("/Users/yan/Documents/Prep/CodeJame/OUT.txt","w", stdout);

    cin >> T;


    for (int x = 1; x <= T; x++)
    {
        cin >> line;
        N = line.size();
        for (int i = 0; i < N; i++)
        {
            if (line[i] == '+'){
                states[i] = true;
            }else{
                states[i] = false;
            }
        }

        //-----------------------------
        int ind = N-1, movee, counter = 0;
        while (ind >= 0)
        {
            //cout << "# flips: " << counter << endl;
            //coutStates();
            movee = nextMove(ind);
            //cout << movee << endl;
            //cout << movee << endl;
            if (movee == -2){
                ind--;
            }else if (movee == -1){
                flip(ind);
                ind--;
                counter++;
            }else {
                //cout << movee << endl;
                flip(movee);
                counter++;
            }
        }

        cout << "Case #" << x << ": " << counter << endl;

        memset(states, 0, sizeof states);

    }
}
