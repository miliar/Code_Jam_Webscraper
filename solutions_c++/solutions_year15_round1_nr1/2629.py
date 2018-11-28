#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int case_num=0; case_num < T; case_num++) {
        int i;
        cin >> i;
        int *counts = new int[i];
        for(int j=0; j < i; j++)
            cin >> counts[j];
        int methodA = 0;
        // In any case where this one is greater than the next one, add the difference to the total
        for(int j=0; j < i-1; j++) {
            if(counts[j+1] < counts[j])
                methodA += counts[j]-counts[j+1];
        }

        int methodB=0;
        // The constant rate can be calculated by the most eaten/10, then add that as a max for each sample where it's less than 10
        int max_consumed=0;
        for(int j=1; j < i; j++) {
            int diff = counts[j-1]-counts[j];
            if(diff > max_consumed)
                max_consumed=diff;
        }

        double rate = max_consumed/10;
        for(int j=0; j < i-1; j++) {
            if(counts[j] > max_consumed)
                methodB += max_consumed;
            else
                methodB += counts[j];
        }

        delete counts;

        cout << "Case #" << case_num+1 << ": " << methodA << " " << methodB << endl;
    }
}
