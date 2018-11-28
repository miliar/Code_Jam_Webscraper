#include <iostream>
#include <queue>
#include <cstdio>
#include <sstream>
#include <utility>

using namespace std;


class CompareDist
{
public:
    bool operator()(pair<int,char> n1,pair<int,char> n2) {
        return n1.first < n2.first;
    }
};
int main(){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		int n;
		cin >> n;
		int aa;
		pair<int, char> a, b;
		char ax = 'A';
		priority_queue<pair<int,char>,vector<pair<int,char> >,CompareDist> pq;
		while(n > 0){
			cin >> aa;
			pq.push(make_pair(aa, ax));
			ax++;
			n--;
		}
		cout << "Case #" << i << ": ";
		bool esp = false;
		while(!pq.empty()){
			if(esp){
				cout << " ";
			}else{
				esp = true;
			}
			

			a = pq.top();
			pq.pop();
			b = pq.top();
			pq.pop();
			if(a.first == 1 && b.first == 1 && pq.size() > 0){
				a.first--;
				cout << a.second;
			}else if(a.first - 1 > b.first){
				a.first -= 2;
				cout << a.second << a.second;
			}else{
				a.first--;
				b.first--;
				cout << a.second << b.second;
			}
			if(a.first > 0){
				pq.push(a);
			}
			if(b.first > 0){
				pq.push(b);
			}

		}
			cout << endl;
	}
	return 0;
}