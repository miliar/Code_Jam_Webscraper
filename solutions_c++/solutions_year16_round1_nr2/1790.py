#include <iostream> 
#include <fstream> 
#include <math.h>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

string intToString (int a)
{
    ostringstream temp;
    temp<<a;
    return temp.str();
}

void print(vector<int> v){
	for (int i = 0; i < v.size(); i++)
		cout << v[i] << " ";
	cout << "\n";
}

string solve(vector<int> v){
	vector<int> h(25000, 0);
	string s = "";
	
	for (int i = 0; i < v.size(); i++)
		h[v[i]]++;
	
	for (int i = 0; i < h.size(); i++)
		if (h[i] % 2 == 1)
			s = s + intToString(i) + " ";
	
	return s;
}


int main() {	
	ifstream input("B-large.in");
	ofstream output("output.ou");

	int sets, n;
	
	if(input.is_open()){
		input >> sets;
		n = 1;
		
		while(sets > 0){
			int N;
			vector<int> list;
			vector<vector<int> > lists;
			
			
			input >> N;
			
			for (int i = 0; i < 2 * N * N - N; i++){
				int temp;
				input >> temp;
				list.push_back(temp);
			}
			
			cout << "Case #" << n << ": " << solve(list) << "\n";
			output << "Case #" << n << ": " << solve(list) << "\n";
			
		
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
