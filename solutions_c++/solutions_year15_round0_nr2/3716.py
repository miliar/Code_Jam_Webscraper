// Example program
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int fastest_time(vector<int> &foods)  {
    int max = foods[foods.size()-1];
    
    int sum;
    int m = max;
    for(int i = 1; i <= max; i++) {
        sum = i;
        for(int j = 0; j < foods.size(); j++) {
            if(foods[j] > i) {
                if(foods[j]%i == 0) {
                    sum += (foods[j]/i-1);
                }
                else {
                    sum += (foods[j]/i);
                }
            }
        }
        m = min(m, sum);
    }

    return m;
}

int main()
{
    int c;
    cin >> c;
    int n = c;
    while(c > 0) {
        int nonempty;
        cin >> nonempty;
        vector<int> foods;
        while(nonempty > 0) {
            int food;
            cin >> food;
            foods.push_back(food);
            nonempty--; 
        }
        sort(foods.begin(), foods.end());
        cout << "Case #" << n - c + 1 << ": " << fastest_time(foods) << endl;
        c--;
    }
    return 0;
}
