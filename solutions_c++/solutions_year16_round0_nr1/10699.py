// counting sheep

#include <iostream>
using namespace std;

void set_array(int arr[],int &cnt, long long int temp) {
    while (temp) {
        //cout << temp % 10 << " " << endl;
        if (arr[temp % 10] == 0) {
            arr[temp % 10] = 1;
            cnt++;
        }
        temp /= 10;
    }

    return ;
}

void get_output (int id, long long int temp) {
    if (temp == 0) {
        cout << "case #" << id << ": " << "INSOMNIA" << endl;
        return ;
    }

    int arr[10], cnt = 0, i = 1;
    for (int i = 0; i < 10; i++)
        arr[i] = 0;

    while (cnt != 10) {
        set_array (arr, cnt, temp * i);
        //cout << temp * i << " " << cnt << endl;
        i++;
    }
    cout << "case #" << id << ": " << --i * temp << endl;

    return ;
}

int main () {
    int n;
    long long int temp;
    cin >> n;

    for (int i = 0 ; i < n; i++) {
        cin >> temp;
        get_output (i + 1, temp);
    }

    return 0;
}
