#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <fstream>
using namespace std;

int main()
{
    ifstream cin("input.in");
    ofstream cout("output.out");
    int t;
    cin >> t;
    for(int a = 0;a<t;a++){
        int n;
        cin >> n;
        vector<int> Diners(n);
        for(int i = 0;i<n;i++){
            cin >> Diners[i];
        }
        int ans = 1010;
        for(int mid = 1;mid <= 1000;mid++){
            int sum = mid;
            for(int i = 0;i<n;i++){
                sum += ceil((double)Diners[i]/(double)mid)-1;
            }
            ans = min(ans,sum);
        }
        cout << "Case #"<< a+1 <<": "<< ans <<"\n";
    }
    return 0;
}
