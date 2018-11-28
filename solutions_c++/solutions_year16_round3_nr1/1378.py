#include <iostream>
#include <set>
#include <vector>
#include <map>

using namespace std;

const int MAXN = 1e3 + 123;


map <char, int> count;

struct compare {
    bool operator() (const char& lhs, const char& rhs) const{
        if(count[lhs] == count[rhs])
        	return lhs < rhs;
        return count[lhs] < count[rhs];
    }
};

set<char, compare> st;

int main(){
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		count.clear();
		st.clear();
		int n;
		cin >> n;
		int total = 0;
		for (int i = 0; i < n; ++i)
		{
			int inp;
			cin >> inp;
			total += inp;
			char c = 'A' + i;
			count[c] = inp;
			st.insert(c);
		}
		vector<string> result;
		while(total > 0){
			string res = "";
			char c = *st.rbegin();
			st.erase(c);
			count[c] --;
			st.insert(c);
			total --;

			res += c;
			int bigR = count[*st.rbegin()];
			
			if(total > 0 && 2 * bigR > total){
				char c2 = *st.rbegin();
			st.erase(c2);
			count[c2] --;
			st.insert(c2);
			total --;
			res += c2;
			
			}
			result.push_back(res);
		}
		cout << "Case #" << test+1 << ": ";
		for (int i = 0; i < result.size(); ++i)
		{
			cout << result[i] << " ";
		}
		cout << endl;

	}

	return 0;
}