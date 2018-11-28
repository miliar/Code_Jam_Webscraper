#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
    int Z;
    vector<int> motes;
    cin >> Z;
    for(int i =0; i < Z; i++)
    {
            int A, N;
            cin >> A >> N;
            for(int j = 0; j < N; j++)
            {
                    int mote_size;
                    cin >> mote_size;
                     motes.push_back(mote_size);
            }
            int min = N;
            sort(motes.begin(), motes.end());
            int Acopy = A;
            if(A > 1)
            {
                for(int j = -1; j < N; j++)
                {
                        int moves = 0;
                        for(int k = 0; k <= j; k++)
                        {
                                while(A <= motes[k]) 
                                {
                                     A += (A-1);
                                     moves++;
                                }
                                A += motes[k];
                        }
                        moves += N - j - 1;
                        if(moves < min) min = moves;
                        A = Acopy;
                }
            }
            motes.clear();
            cout << "Case #" << i + 1 << ": " << min << endl;
    }
    return 0;
}
