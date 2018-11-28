#include <iostream>
#include <string>
using namespace std;


string repS1(string s1, int a1[]) {
	string ret;
	int j =0;
	int curr=0;
	while(curr<s1.size()) {
		int start = curr;
		int count=0;
		while (curr < s1.size() && s1[start]==s1[curr]){
			curr++;
			count++;
		}
		a1[j]=count;
		ret += s1[start];
		j++;
	}
	return ret;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,N;
	cin >> T;
	int a[101];
	int a2[101];
	int count;
	string s;
	for (int t=0; t<T; t++) {
		count=0;
		cin >> N;
		cin >> s;
		string ret1 = repS1(s,a);
		cin >> s;
		string ret2 = repS1(s,a2);
		if (ret1!=ret2) cout << "Case #" << t+1 << ": " << "Fegla Won" << endl;
		else {
			for (int i=0; i<ret1.size(); i++) {
				count+=abs(a[i]-a2[i]);
			}
			cout << "Case #" << t+1 << ": " << count << endl;
		}
	}

}