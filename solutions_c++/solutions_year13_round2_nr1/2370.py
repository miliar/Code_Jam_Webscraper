#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int Solve(long long int A, vector<long long int>& motes)
{
    sort(motes.begin(), motes.end());
    // Going with the greedy approach
    // if the next mole is not abosorbable insert one of the value (A-1)
    // it it is still not absorbable, delete it, otherwise keep the inserted one and absorb the next
    int deletes = 0, inserts = 0;

    for (int i = 0; i < motes.size(); ++i) {
        if (A <= motes[i]) {
            // del = Compute number of deletes needed if we don't insert anything
            // If we decide to delete this elements we will delete next as well (array is sorted)
            int del = motes.size() - i;

            // ins = Compute number of inserts needed to absorb the next element
            long long int diff = motes[i] - A;
            long long int a = A;
            int ins = 0;
            while (a <= motes[i] && ins < del) {
                a += a-1;
                ++ins;
            }

            if (del > ins) { // we must insert
                A = a;
                inserts += ins;
            } else { // we must delete
                deletes += del;
                break;
            }
        }
        A = A + motes[i];
    }

    return (deletes + inserts);
}



int main(void)
{
    int T, i = 1;
    cin >> T;
    while (T--) {
        long long int A, N;
        vector<long long int> motes;
        cin >> A >> N;
        while (N--) {
            long long int s;
            cin >> s;
            motes.push_back(s);
        }
        cout << "Case #" << i++ << ": " << Solve(A, motes) << endl;
    }
    return 0;
}
