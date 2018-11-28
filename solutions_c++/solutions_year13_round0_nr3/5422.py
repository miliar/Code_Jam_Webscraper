#include <iostream>
#include <vector>
using namespace std;

vector <int> v;

bool isP(long long int n){
    int d[15];
    int count = 0;
    for(count = 0 ; count < 15 ; count++){
        d[count] = n % 10;
        n/=10;
        if (n == 0)
          break;
    }
    for (int i = 0 ; i < count ; i++)
        if (d[i] != d[count-i]){
            return false;
        }
    return true;
}

int main (){
    long long int i = 0;
    long long limit = 10000000;
    while (i < limit) {
        if (isP(i)&&isP(i*i))
            v.push_back(i*i);
        i++;
    }
    long long int T, start, end;
    int cnt;
    cin >> T;
    int t =0 ;
    while (T--){
        t++;
        cin >> start >> end;
        cnt = 0;
        for (int i = 0 ; i < v.size(); i++)
            if (v[i]>=start && v[i]<=end)
                cnt++;
        cout << "Case #" << t << ": " << cnt << endl;
    }
}