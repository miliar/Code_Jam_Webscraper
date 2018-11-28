#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#define MAXIM 1000002

using namespace std;

map<string,int> arr;

void display(vector<int> p, int ans)
{
	cout << endl;
	for(int i = 0; i < p.size(); ++i){
		cout << p[i] << " ";
	}
	cout << endl << "ans = " << ans << endl << endl;
}

int getAns(vector<int> p)
{
	string s;
	sort(p.begin(), p.end(),greater<int>());
	for(int i = 0; i < p.size(); ++i){
		//cout << p[i] << ",";
		char c = p[i] + '0';
		if(p[i] == 0)
			break;
		s += c;
	}
	//cout << endl << s << endl;
	if(arr[s] > 0)
		return arr[s];
	int ans = 0, ans2,  min_ans = p[0];
	if(p[0] <= 3){
		ans += p[0];
		arr[s] = ans;
		return ans;
	}
	vector<int> q;
	for(int i = 0; i < p.size(); ++i){
		if(p[i])
			q.push_back(p[i]-1);
		else
			q.push_back(0);
	}
	ans2 = ans + 1 + getAns(q);
	//	cout << "ans2 for " << s << " = " << ans2 << endl;
	if(ans2 < min_ans)
		min_ans = ans2;
	int mid = p[0]/2, p_0 = p[0];
	for(int i = 1; i <= mid; ++i){
		vector<int> z(p.begin(), p.end());
		z.push_back(p[0] - i);
		z[0] = i;
		ans2 = ans + 1 + getAns(z);
		if(ans2 < min_ans)
			min_ans = ans2;
	}
	arr[s] = min_ans;
	//cout << "Stored arr[" << s << "] = " << min_ans << endl;
	return min_ans;
}



int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t){
		arr.clear();
		int d;
		cin >> d;
		vector<int> p;
		for(int i = 0; i < d; ++i){
			int cake;
			cin >> cake;
			p.push_back(cake);
		}
		cout << "Case #" <<  t << ": " << getAns(p) << endl;
	}
}