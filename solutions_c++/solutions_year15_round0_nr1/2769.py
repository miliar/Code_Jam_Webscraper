#include<fstream>
#include<string>
#include<sstream>

using namespace std;

int main(){
	ifstream in("a.in");
	ofstream out("a.out");
	int T;
	in >> T;
	for (int i = 0; i < T; i++){
		int N;
		in >> N;
		string line;
		in >> line;
		//out << "N=" << N<<endl;
		//out << "line=" << line << endl;
		int *shyness = new int[N+1]();
		int sum = 0;	//number of audience who have standed up
		int friends_num = 0;
		for (int j = 0; j <=N; j++){
			shyness[j] = line[j]-48;
			//out << shyness[j] << endl;
			int need = j - sum;
			if (need > 0&&shyness[j]>0){
				friends_num += need;
				sum += friends_num;
			}
			sum += shyness[j];
		}
		out << "Case #" << i + 1 << ": " << friends_num << endl;
	}
	return 0;
}