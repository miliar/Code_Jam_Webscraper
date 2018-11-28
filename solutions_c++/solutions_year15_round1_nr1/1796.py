#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("input.in");
    ofstream cout("output.out");
    int t;
    cin >> t;
    int A[1010];
    for(int a = 0;a<t;a++){
        int n; cin >> n;
        int ansA = 0;
        int MaxDiff = 0;
        cin >> A[0];
        for(int i = 1;i<n;i++){
            cin >> A[i];
            ansA += max(0,A[i-1]-A[i]);
            MaxDiff = max(MaxDiff,A[i-1]-A[i]);
        }
        int ansB = 0;
        for(int i = 1;i<n;i++){
            ansB += min(A[i-1],MaxDiff);
        }
        cout << "Case #"<<a+1<<": "<< ansA << " " << ansB<<"\n";
    }
    return 0;
}
