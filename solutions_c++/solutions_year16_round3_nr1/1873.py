#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    for(int k = 0; k < n; k++){
        int numParties;
        cin >> numParties;
        vector<int> inside(numParties, 0);
        int sum = 0;
        int max1 = -1;
        int max2 = -1;
        for(int i = 0; i < numParties; i++){
            cin >> inside[i];
            // cerr << inside[i];
            sum += inside[i];
            if(inside[i] > (max1 == -1 ? -1 : inside[max1])){
                max2 = max1;
                max1 = i;
            }
            else if(inside[i] > (max2 == -1 ? -1 : inside[max2])){
                max2 = i;
            }
        }
        cerr << max1 << max2 << endl;

        vector <int> soln;
        while(inside[max1] != inside[max2]){
            sum--;
            soln.push_back(inside[max1] > inside[max2] ? max1: max2);
            inside[inside[max1] > inside[max2] ? max1 : max2]--;
        }
        while(sum > inside[max1] + inside[max2]){
            for(int i = 0; i < numParties; i++){
                if(inside[i] && i != max1 && i != max2){
                    sum--;
                    inside[i]--;
                    soln.push_back(i);
                }
            }
        }
        cout << "Case #" << k+1 << ":";
        for(auto i : soln){
            cout << " ";
            cout << char('A' + i);
        }
        while(sum){
            sum -= 2 ;
            // cerr << max1 << max2 << endl;
            cout << " " << char('A' + max1) << char('A' + max2);
        }
        cout << endl;
    }
}
