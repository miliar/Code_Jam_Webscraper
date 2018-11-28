#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std;

class solution{
public:
	solution(char *input, char *output){
		ifs.open(input);
		ofs.open(output);
		n = 0;
	}

	~solution(){
		ifs.close();
		ofs.close();
	}

public:
	void read(){
		ifs>>n;
		int tmp1,tmp2;
		for (int i = 0; i < n; ++i){
			ifs>>tmp1;
			ifs>>tmp2;
			string s = to_string(tmp2);
			if(s.size() < tmp1+1)
				s.insert(0, tmp1+1-s.size(), '0');
			m[i+1] = make_pair(tmp1,s);
		}
	}

	void write(){
		for (int i = 0; i < n; ++i)
			ofs<<"Case #"<<i+1<<": "<<res[i]<<endl;
	}

	int calculate(int nth){
		int max_shy = m[nth].first;
		string audience = m[nth].second;
		int n_friend = 0, n_standUp = 0;
		for (int i = 0; i <= max_shy; ++i){
			if(n_standUp < i){
				n_friend += i-n_standUp;
				n_standUp = i;
			}
			n_standUp += audience[i]-'0';
		}
		return n_friend;
	}

	void getRes(){
		for (int i = 0; i < n; ++i){
			int res_i = calculate(i+1);
			res.push_back(res_i);
		}
	}

private:
	ifstream ifs;
	ofstream ofs;
	int n;
	map<int, pair<int, string> > m;
	vector<int> res;
};


void main(){
	solution s("A-small-attempt0.in", "output.txt");
	s.read();
	s.getRes();
	s.write();
}
