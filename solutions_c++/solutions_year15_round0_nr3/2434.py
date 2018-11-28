#include<fstream>
#include<string>
#include<vector>
#include<cmath>

using namespace std;

int data[5][5] = {
	{0,0,0,0,0},
	{0,1,2,3,4},
	{0,2,-1,4,-3},
	{0,3,-4,-1,2},
	{0,4,3,-2,-1} 
};

bool equalOne(vector<int> line, long i){
	long length = line.size();
	int ans;
	for (; i < length-1; i++){
		ans = data[abs(line[i])][abs(line[i+1])];
		if (line[i] < 0)
			ans = -ans;
		if (line[i+1] < 0)
			ans = -ans;
		line[i+1] = ans;
	}
	return line[i] == 1;
}

int main(){
	ifstream in("c1.in");
	ofstream out("c1.out");
	int T;
	in >> T;
	for (int t = 1; t <= T; t++){
		bool flag = false;
		long L, X;
		in >> L >> X;
		string s;
		in >> s;
		vector<int> vec(L);
		for (long i = 0; i < s.length(); i++){
			if (s[i] == 'i')
				vec[i] = 2;
			else if (s[i] == 'j')
				vec[i] = 3;
			else if (s[i] == 'k')
				vec[i] = 4;
		}
		long total_length = L*X;
		vector<int> line(total_length);
		for (int i = 0; i < total_length; i++){
			line[i] = vec[i%L];
			//cout << line[i];
		}
		/*cout << endl;*/
		int result = 2;
		for (long index = 0; index <total_length; index++){
			long i = index;
			int ans = line[i];
			if (ans == result){
				//cout << "Pair! " <<index<< endl;
				result++;
				if (result == 5){
					//totoal是index的整倍数
					if (index+1==total_length)
						flag = true;
					else if(equalOne(line,index+1)){
						flag = true;
					}
					break;
				}
				continue;
			}
			int j = i + 1;
			if (j >= total_length)
				break;
			ans = data[abs(line[i])][abs(line[j])];
			if (line[i] < 0)
				ans = -ans;
			if (line[j] < 0)
				ans = -ans;
			line[j] = ans;
			/*cout << "ans=" << ans << endl;*/

		}
		out << "Case #" << t << ": " << (flag ? "YES" : "NO" )<< endl;
	}
}