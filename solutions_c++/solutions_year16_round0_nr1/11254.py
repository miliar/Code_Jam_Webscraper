#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Nodes{
	unsigned int N;
	vector<int> nodes_visited;
	vector<vector<int>> consective_result;
	const unsigned int CONSECUTIVE_SIZE = 20;
	const unsigned int MAX_CONSECUTIVE = 15;
	bool check_value(int N){
		if ((0 <= N) && (N <= 1000000))
			return 1;
		else
			return 0;
	}
	bool compare_two_vectors(vector<int> first, vector<int> second){
		if (first.size() != second.size())
			return false;
		else
			for (unsigned int i = 0; i < first.size(); i++){
				if (first[i] != second[i])
					return false;
			}
		return true;
	}
	int is_repeated(){
		unsigned int repeat_count = 0;
		for (unsigned int i = 0; i < (CONSECUTIVE_SIZE-MAX_CONSECUTIVE) && i<consective_result.size(); i++){
			for (unsigned int j = i + 1; j < CONSECUTIVE_SIZE && j < consective_result.size(); j++){
				if (compare_two_vectors(consective_result[i], consective_result[j]))
					repeat_count++;
			}
			if (repeat_count > MAX_CONSECUTIVE)
				return true;
			repeat_count = 0;
		}
		if (repeat_count > MAX_CONSECUTIVE)
			return true;
		return false;
	}
	bool is_unique(int temp){
		if (!nodes_visited.size())
			return true;
		for (unsigned int i = 0; i < nodes_visited.size(); i++)
			if (nodes_visited[i] == temp)
				return false;
		return true;
	}
	bool add_n_check_list(unsigned long int num){
		int temp = 0;
		vector<int> temp_buf;
		while (num){
			temp = num % 10;
			num = num / 10;
			if (is_unique(temp)){
				nodes_visited.push_back(temp);
			}
			temp_buf.push_back(temp);
		}
		if (consective_result.size() > CONSECUTIVE_SIZE){
			consective_result.erase(consective_result.begin());
		}
		consective_result.push_back(temp_buf);
		return true;
	}
	void display(){
		for (unsigned int i = 0; i < nodes_visited.size(); i++)
			cout << nodes_visited[i] << endl;
	}
	bool is_complete(){
		for (int i = 0; i < 10; i++)
			if (is_unique(i))
				return false;
		return true;
	}
public:
	bool static check_testcase(int T){
		if ((1 <= T) && (T <= 100))
			return 1;
		else
			return 0;
	}
	bool AddNode(int numb_to_add){
		if (check_value(numb_to_add))
			N = numb_to_add;
		else
			return 0;
		return 1;
	}
	unsigned int getValue(){
		return N;
	}
	string process(){
		//add_n_check_list(N);
		/*if (is_complete()){
		display();
		return;
		}*/
		unsigned long int temp = N;
		unsigned int max_size = 1 << (sizeof(int) * 8 - 1);
		for (unsigned int i = 1; i < max_size; i++){
			temp = i*N;
			add_n_check_list(temp);
			if (is_complete()){
				return std::to_string(temp) + to_string(i);
			}
			if (is_repeated())
				return "INSOMNIA";
		}
		//display();
		return "INSOMNIA";
	}
	bool static isExists(vector<Nodes> &Nodes_, unsigned int numb){
		for (unsigned int i = 0; i < Nodes_.size(); i++)
			if (Nodes_[i].getValue() == numb)
				return true;
		return false;
	}

};
int main(){
	vector<Nodes> N;
	unsigned int T = 0, tempN;
	Nodes temp;
	cin >> T;
	if (!Nodes::check_testcase(T))
		return -2;
	for (unsigned int i = 0; i < T; i++){
		cin >> tempN;
		if (Nodes::isExists(N, tempN) || !temp.AddNode(tempN))
			return -1;
		N.push_back(temp);
	}
	for (unsigned int i = 0; i < T; i++){
		cout << "Case #" << (i + 1) << ": " << "" << N[i].process() << endl;
		//N[i].process();
	}
}