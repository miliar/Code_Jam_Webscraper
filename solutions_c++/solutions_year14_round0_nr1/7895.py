/*
#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int T, n, *store, sum, average, account, sender, money;
  cin >> T;
  while (T--) {
    cin >> n;
    store = new int[n];
    sum = 0;
    account = 0;
    money = 0;
    for (int i = 0; i < n; i++) {
      cin >> store[i];
      sum += store[i];
    }
    average = sum / n;
    for (int i = 0; i < n; i++) {
      store[i] -= average;
      if (store[i] == 0) account++;
    }
    
    //
    for (int i = 0; i < n; i++) {
      cout << store[i] << " ";
    }
    cout << endl;
    
    sender = 0;
    while (account < n) {
      while (store[sender] <= 0)
        sender = (sender + 1) % n;
      cout << "sender: " << sender << endl; //
      int receiver = (sender + 1) % n, distance = 1;
      cout << "receiver: " << receiver << endl; //
      cout << "distance: " << distance << endl; //
      while (store[sender] != 0) {
        while (store[receiver] >= 0) {
          receiver = (receiver + 1) % n;
          distance++;
        }
        cout << "store[sender]: " << store[sender] << endl; //
        cout << "store[receiver]: " << store[receiver] << endl; //
        if (store[sender] + store[receiver] > 0) {
          money += abs(store[receiver]) * distance;
          store[sender] += store[receiver];
          store[receiver] = 0;
          account++;
          cout << "possibility 1\n";
          cout << "store[sender]: " << store[sender] << endl; //
          cout << "store[receiver]: " << store[receiver] << endl; //
        } else if (store[sender] + store[receiver] == 0) {
          money += abs(store[receiver]) * distance;
          store[sender] =0;
          store[receiver] = 0;
          account += 2;
          cout << "possibility 2\n";
          cout << "store[sender]: " << store[sender] << endl; //
          cout << "store[receiver]: " << store[receiver] << endl; //
        } else {
          money += abs(store[sender]) * distance;
          store[receiver] += store[sender];
          store[sender] = 0;
          account++;
          cout << "possibility 3\n";
          cout << "store[sender]: " << store[sender] << endl; //
          cout << "store[receiver]: " << store[receiver] << endl; //
        }
      }
    }
    cout << money << endl;
    
    delete [] store;
  }
}
*/

