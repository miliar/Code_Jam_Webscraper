#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

vector<int> findSmallest(vector<int> motes) {
    int smallest = motes[0];
    int index = 0;
    for (int i = 0; i < motes.size(); i++)
        if(motes[i] < smallest) {
            smallest = motes[i];
            index = i;
        }
    
    vector<int> response;
    response.push_back(smallest);
    response.push_back(index);
    
    // cout << "smallest: " << smallest << " at " << index << endl;
    return response;
}

int iterations(int a, int smallest, int size) {
    int i = 0;
    while(a <= smallest && i < size) {
        a += (a-1);
        i++;
    }
    return i;
}

int consume(vector<int> motes, int a, int &counter, int &total) {
    // cout << "consume(" << motes.size() << ", " << a << ", " << counter << endl;
    if(motes.size() == 0)
        return a;
    else {
        vector<int> response = findSmallest(motes);
        if(a > response[0]) {
            a += response[0];
            motes.erase( motes.begin() + response[1] );
            
            return consume(motes, a, counter, total);
        }
        else {
            int diff = a - 1;
            if( (a + diff) > response[0] ) {
                motes.push_back(diff);
            }
            else {
                int cnt = iterations(a, response[0], motes.size());
                
                if(cnt >= motes.size()) {
                    motes.erase( motes.begin() + response[1] );
                    total -= response[0];
                }
                else {
                    motes.push_back(diff);
                }
            }
            
            counter++;
            
            return consume(motes, a, counter, total);
        }
    }
}

int solve(vector<int> motes, int a, int total) {
    // cout << "solve(" << motes.size() << ", " << a << ", " << total << endl;
    int counter = 0;
    int finished = consume(motes, a, counter, total);
    // cout << finished << " ?= " << total << endl;
    if(finished >= total)
        return counter;
    else
        return -1;
}

int main ()
{
    ofstream out;
    out.open("a.out");
    
    int T;
    cin >> T;
    
    cout << "T = " << T << endl;
    
    for(int i = 0; i < T; i++) {
        int A, N;
        
        cin >> A;
        cin >> N;
        
        cout << "Case #" << i+1 << " | A = " << A << " | N = " << N;
        
        vector<int> motes;
        int total = A;
        
        for(int j = 0; j < N; j++) {
            int moteSize;
            cin >> moteSize;
            motes.push_back(moteSize);
            
            total += moteSize;
        }
        
        int solved = solve(motes, A, total);
        
        
        if(solved != -1) {
            cout << " | SOLVED " << solved << endl;
            out << "Case #" << i+1 << ": " << solved << endl;
        }
        else {
            cout << " | FAILED" << endl;
        }
    }
    
    return 0;
}