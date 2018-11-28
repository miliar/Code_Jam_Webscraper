#include<iostream>
#include<algorithm>
using namespace std;

int arr[10] = {0};

void alloc(int x) {
    while (x) {
        arr[x%10] = 1;
        x /= 10;
    }
}

bool check() {
    for (int i = 0;i<10;i++)
        if (arr[i] == 0)    return false; // ! all seen
    return true; // All seen
}

int main() {

    int t,n,ctr,present;
    cin >> t;
    for (int i = 1;i<=t;i++) {
        cin >> n;
        cout << "Case #"<<i<<": ";
        if (n == 0) {cout <<"INSOMNIA\n"; continue;}
        ctr = 1;
        present  = n;

        alloc(present);
        while(check() != true) {
            present = n * (++ctr);
            alloc(present);
        }

        cout <<present<<'\n';

        fill(arr, arr+10, 0);
    }
    return 0;
}
