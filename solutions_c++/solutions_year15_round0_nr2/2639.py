#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;

int calc(vector<int>);

ifstream in("b.in");
ofstream out("b.out");


bool needCut(vector <int> vec){
	int first = vec[0];
	int dif = 0;
	int mid = vec[0] / 2 + vec[0] % 2;
	for (auto e : vec){
		if (e > mid)
			dif++;
	}
	return (mid + dif)<first;
}


int main(){
	int T;
	in >> T;
	for (int t = 0; t < T; t++){
		int N;
		in >> N;
		vector<int> num(N);
		for (int j = 0; j < N; j++){
			in >> num[j];
		}
		sort(num.begin(), num.end(), isgreater<int, int>);
		int max = num[0];
		int min = max;
		int sum = 0;
		for (int i = 1; i <= max; i++) {
			sum = i;
			//out << "i=" << sum << endl;
			for (int j = 0; j < N; j++) {
				//out << num[j] << " ";
				if (num[j] > i) {
					if (num[j] % i == 0)
						sum += (num[j] / i - 1);
					else
						sum += (num[j] / i);
				}
			}
			//out <<endl<< "sum=" << sum << endl;
			if (sum < min)
				min = sum;
		}
		//int ans=calc(num);
		out << "Case #" << t + 1 << ": " << min << endl;
	}
	in.close();
	out.close();
	return 0;
}

int calc(vector<int> num){
	sort(num.begin(), num.end(),isgreater<int,int>);
	//for (auto i : num){
	//	out << i << " ";
	//}
	//out << endl;
	int minutes = 0;
	while (!num.empty())
	{
		if (needCut(num)){
			int mid = num[0] / 2 + num[0] % 2;
			for (int i = 0; i<num.size() && num[i] > mid; i++){
				int a = num[i] / 2 + num[i] % 2;
				num[i] /= 2;
				num.push_back(a);
				minutes++;
			}
			sort(num.begin(), num.end(), isgreater<int, int>);
		}
		else
		{
			vector<int>::iterator it = num.begin();
			for (; it != num.end(); it++){
				(*it)--;
				if (*it == 0){
					num.erase(it, num.end());
					break;
				}
			}
			minutes++;
		}
/*
		for (auto e : num){
			out << e << " ";
		}
		out << endl;*/
	}
	return minutes;
}