#include <iostream>
#include <limits.h>
#include <unordered_map>

using namespace std;

void markCounts (const long long, unordered_map<int,bool>& );

void markCounts (const long long p, unordered_map<int,bool>& h){
    for (int i=p; i>0; i/=10){
        int r = i%10;
        h.emplace(r,1);
	}
}

int main() {
    int N;
    cin >> N;
    for (int iter=1; iter<=N; iter++){
        int n=0, i=0;
        cin >> n;
        long long p=0;
        bool f=0;
        unordered_map<int, bool> h; 
        if (n==0) {
            cout << "Case #"<< iter << ": INSOMNIA" << endl;
            continue;
        }
        while (p<=INT_MAX && f==0){
            p = i*n;
            markCounts (p, h);
            if (h.size() == 10)
                f = 1;
            i++;
        }
        if (p==INT_MAX)
            cout << "Case #"<< iter << ": INSOMNIA" << endl;
        else 
            cout << "Case #"<< iter << ": " << p << endl;
    }
	return 0;
}