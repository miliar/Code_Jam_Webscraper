
#include <iostream>
#include <vector>

using namespace std;


int mark(int number, vector<bool> &visited, int nvisited) {
    while (number > 0) {
        int temp = number%10;
        //cout  << temp  << endl;
        if (!visited[temp]) {
            nvisited++;
            visited[temp] = true;
        }
        number /= 10;
    }
    return nvisited;
}

int count(int num) {
    if (num == 0) return -1;
    vector<bool> visited(10,false);
    int nvisited = 0;
    int number = num;
    while ((nvisited = mark(number, visited, nvisited)) != 10)  {
        number += num;
    }
    return number;
}


int main()
{
    int n;
    cin >> n;
    vector<int> nums(n,0);
    int res;
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    for (int i = 0; i < n; i++) {
        res = count(nums[i]);
        if (res == -1) {
            cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
        } else {
            cout << "Case #" << i+1 << ": " << res << endl;
        }
    }
}
