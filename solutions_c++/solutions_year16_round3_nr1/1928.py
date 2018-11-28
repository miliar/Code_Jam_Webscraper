#include <iostream>
#include <string>
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)

using namespace std;

int main() {
	int t;
	cin >> t;
	F1(i, t) {
		int party_num = 0;
		int people[26] = { 0 };
		int people_num = 0;
		cin >> party_num;
		F0(j, party_num) {
			cin >> people[j];
			people_num += people[j];
		}
		cout << "Case #" << i << ": ";
		while (people_num) {
			if (people_num % 2 == 0) {
				int largest_party[2] = { 0 };
				int largest_people[2] = { 0 };
				F0(k, party_num) {
					if (people[k] > largest_people[0]) {
						largest_people[0] = people[k];
						largest_party[0] = k;
					}
				}
				people[largest_party[0]]--;
				F0(k, party_num) {
					if (people[k] > largest_people[1]) {
						largest_people[1] = people[k];
						largest_party[1] = k;
					}
				}
				people[largest_party[1]]--;
				people_num -= 2;
				
				char p1 = 'A' + largest_party[0];
				char p2 = 'A' + largest_party[1];
				cout << p1 << p2 << ' ';
			}
			else {
				int largest_party = 0;
				int largest_people = 0;
				F0(k, party_num) {
					if (people[k] > largest_people) {
						largest_people = people[k];
						largest_party = k;
					}
				}
				people[largest_party]--;
				people_num--;
				char p1 = 'A' + largest_party;
				cout << p1 << ' ';
			}
		}
		cout << endl;
	}
}