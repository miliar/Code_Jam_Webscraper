#include<iostream>
#include<cstring>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
using namespace std;
long long N, J, T;
int tab[40];

int main(){
	cin >> T;

	for (int t = 0; t < T; ++t) {
		cin >> N;
		map<char, int> m; //priority_queue<int> pq;
		long sum = 0;
		for (int i = 0; i < N; ++i) {
			cin >> tab[i];
			m.insert(std::pair<char, int>('A'+i, tab[i]));
			sum += tab[i];
		};
		cout << "Case #" << t+1 << ": ";
		while (sum>0) {
/*			for (auto x : m) {
				cout << endl << ":: " << x.first << " = " << x.second << endl;
			};*/
			if (m.size() == 1) { //tylko 1 partia
				//?? 
			};
//----
std::vector<pair<char, int>> v;
for (auto itr = m.begin(); itr != m.end(); ++itr)
	    v.push_back(*itr);


struct sort_pred {
	    bool operator()(const std::pair<char,int> &left, const std::pair<char,int> &right) {
		            return left.second > right.second;
			        }
};

std::sort(v.begin(), v.end(), sort_pred());
/*
sort(pairs.begin(), pairs.end(), [](pair<char, int>& a, pair<char, int>& b)
     {
	         return a.second < b.second;
     });*/
//----

			auto a = v.begin();
			char a_partia = a->first;
			int a_ile = a->second;
			a++;
			char b_partia = a->first;
			int b_ile = a->second;
			if (a_ile < 2){
				if (sum == 2) {
					cout << a_partia << b_partia << " ";
					m.erase(a_partia); 
					m.erase(b_partia);
					sum-=2;
				} else {
					cout << a_partia << " ";
					m.erase(a_partia);
					sum-=1;
				};
			} else {
				float diff = float(b_ile) / ((float)(sum-2));
				if (diff < 0.5) {
					cout << a_partia << a_partia << " ";
					m.erase(a_partia);
					if (a_ile > 2) m.insert(std::pair<char, int>(a_partia, a_ile-2));
				} else {
					cout << a_partia << b_partia << " ";
					m.erase(a_partia);
					if (a_ile > 1) m.insert(std::pair<char, int>(a_partia, a_ile-1));
					m.erase(b_partia);
					if (b_ile > 1) m.insert(std::pair<char, int>(b_partia, b_ile-1));
				};
				sum-=2;
			};
		};
		cout <<endl;

	};
};
