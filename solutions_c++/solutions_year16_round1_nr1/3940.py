/*
	Alexandre Borgo - Google Code Jam - 2016 -
*/

#include <iostream>
#include <vector>

using namespace std;

int main() {
  int T;
  int n;
  int j;

  cin >> T;

  for(int i = 1 ; i <= T ; i++) {

    string l = "";

    cin >> l;

    vector<char> result;
    result.push_back(l.at(0));

    for(int i = 1 ; i < l.size() ; i++) {
        //cout << result.at(0) << " " << l.at(i) << endl;
        if(result.at(0) <= l.at(i)) {
            result.insert(result.begin(),l.at(i));
        }
        else {
            result.push_back(l.at(i));
        }
    }

    cout << "Case #" << i << ": ";
    for(int z = 0 ; z < result.size() ; z++)
        cout << result[z];
    cout << endl;

  }

  return 0;
}
