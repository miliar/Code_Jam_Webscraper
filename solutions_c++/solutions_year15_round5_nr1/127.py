
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <utility>
using namespace std;

#define range(i,a,b) for(int i = (a), _n = (b); i < _n; ++i)
#define fo(i,n) range(i, 0, n)

typedef long long ll;
typedef pair<ll, ll> pr;

const int MAX_N = 1100100, MAX_D = 1100100;

ll S0, AS, CS, RS;
ll M0, AM, CM, RM;
ll N, D;
int parent[MAX_N];
ll salary[MAX_N];
bool employed[MAX_N], fired[MAX_N];
vector<int> children[MAX_N];

#define _salary first
#define _person second

int employ(int i) {
	if (employed[i] || fired[i]) return 0;
	int count = 0;
	stack<int> todo;
	todo.push(i);
	while(todo.size()) {
		int j = todo.top(); todo.pop();
		if (employed[j] || fired[j]) {
		} else {
			employed[j] = true;
			count += 1;
			fo(k, children[j].size()) todo.push(children[j][k]);
		}
	}
	return count;
}

int unemploy(int i) {
	if (!employed[i] || fired[i]) return 0;
	int count = 0;
	stack<int> todo;
	todo.push(i);
	while(todo.size()) {
		int j = todo.top(); todo.pop();
		if (!employed[j] || fired[j]) {
		} else {
			employed[j] = false;
			count += 1;
			fo(k, children[j].size()) todo.push(children[j][k]);
		}
	}
	return count;
}

int solve() {
	fo(i,N) children[i] = vector<int>();
	range(i,1,N) children[parent[i]].push_back(i);
	
	vector<pr> people;
	fo(i,N) people.push_back(pr(salary[i], i));
	sort(people.begin(), people.end());

	fo(i,N) employed[i] = false, fired[i] = true;

	int start = 0, end = 0, current = 0, best = 1;

	while (end < N) {
		if (people[end]._salary - people[start]._salary <= D) {
			fired[people[end]._person] = false;
			if (people[end]._person == 0 || employed[parent[people[end]._person]]) {
				current += employ(people[end]._person);
			}
			//cout << "employed up to " << current << ", " << start << ' ' << end << endl;
			++end;
		} else {
			current -= unemploy(people[start]._person);
			fired[people[start]._person] = true;
			//cout << "unemployed down to " << current << ", " << start << ' ' << end << endl;
			++start;
		}
		//fo(i,N) cout << employed[i] << ' '; cout << endl;
		//fo(i,N) cout << fired[i] << ' '; cout << endl;
		best = max(current, best);
	}

	return best;
}

int main() {

	int T;
	cin >> T;
	range(testCase, 1, T+1) {
		cin >> N >> D;
		cin >> S0 >> AS >> CS >> RS;
		cin >> M0 >> AM >> CM >> RM;

		ll s = S0, m = M0;
		salary[0] = s;
		parent[0] = -1;
		range(i, 1, N) {
			s = (s * AS + CS) % RS;
			m = (m * AM + CM) % RM;
			salary[i] = s;
			parent[i] = m % i;
		}

		cout << "Case #" << testCase << ": " << solve() << endl;
	}

}
