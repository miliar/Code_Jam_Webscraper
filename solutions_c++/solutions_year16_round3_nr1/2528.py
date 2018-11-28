#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;

struct Pair{
    char name;
    int count;
};

vector<Pair> data;
void add(Pair item){
    int n = 0;
    while(n < data.size() && item.count < data[n].count)
        n++;
    data.insert(data.begin() + n, item);
}

void normalize(){
    int m;
    Pair temp;
	for (int n = 0; n < data.size(); n++){
		m = n;
		while (m > 0 && data[m].count > data[m-1].count){
			  temp = data[m];
			  data[m] = data[m-1];
			  data[m-1] = temp;
			  m--;
          }
      }
}


int main() {
    freopen("out.txt", "w", stdout);
    int T, N;
    int space = 0;
    cin >> T;

    for(int t = 0; t < T; t++){
        cin >> N;
        space = 0;
        data.clear();
        for(int n = 0, a; n < N; n++){
            cin >> a;
            add({n + 'A', a});
        }

        cout << "Case #" << (t+1) << ": ";
        while(data.size() > 0){
            if(space == 2){
                cout << ' ';
                space = 0;
            }
            if(data.size() == 3){
                if(data[0].count * data[1].count * data[2].count == 1){
                    cout << data[0].name;
                    data.erase(data.begin());
                    space = 2;
                    continue;
                }
            }
            cout << data[0].name;
            data[0].count--;

            if(data[0].count == 0)
                data.erase(data.begin());
            if(data.size() == 0)
                break;
            space++;
            normalize();
        }
        cout << endl;
    }

    return 0;
}
