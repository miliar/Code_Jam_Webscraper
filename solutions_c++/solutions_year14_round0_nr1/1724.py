#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <time.h>

using namespace std;

template<typename T>
void print(const vector<vector<T>> &tb){
	for (int i=0; i!=tb.size(); ++i){
		vector<T> row = tb[i];
		for (int j=0; j!=row.size(); ++j)
			cout<<row[j]<<" ";
		cout<<endl;
	}
}

template<typename T>
void print(const vector<T> &a){
	for (int j=0; j!=a.size(); ++j)
		cout<<a[j]<<" ";
	cout<<endl;
}

vector<int> splitString(string str, char delim){
	vector<int> vec;
	string item;
	stringstream sstr = stringstream(str);
	while(getline(sstr, item, delim)){
		vec.push_back(stoi(item));
	}
	return vec;
}

typedef vector<vector<int>> matrix2D;

int main() {
	clock_t t1 = clock();
    ifstream infile("A-small-attempt0.in");
	ofstream outfile("A.out");
	
	int T;
	string instr;
	getline(infile, instr);
	T = stoi(instr);
	cout<<T<<endl;
	matrix2D originalCard(4, vector<int>(4));
	matrix2D shuffledCard(4, vector<int>(4));
	int oriR, sfdR;
	for(int t=0; t!=T; t++){
		getline(infile, instr);
		oriR = stoi(instr);

		for(int r=0; r!=4; r++){
			getline(infile, instr);
			string item;
			int c=0;
			stringstream sstr = stringstream(instr);
			while(getline(sstr, item, ' ')){
				originalCard[r][c++] = stoi(item);
			}
		}

		getline(infile, instr);
		sfdR = stoi(instr);

		for(int r=0; r!=4; r++){
			getline(infile, instr);
			stringstream sstr = stringstream(instr);
			string item;
			int c=0;
			while(getline(sstr, item, ' ')){
				shuffledCard[r][c++]= stoi(item);
			}
		}

		int ct=0, cardN = 0;
		for(int oix = 0; oix!=4; oix++){
			for(int six = 0; six!=4; six++){
				if(originalCard[oriR-1][oix] == shuffledCard[sfdR-1][six]){
					ct++;
					cardN = shuffledCard[sfdR-1][six];
					//cout<<"Case # "<<t+1<<", card "<<cardN<<" is one ans"<<endl;
					break;
				}
			}
		}

		if(ct==0)
			outfile<<"Case #"<<t+1<<": Volunteer cheated!"<<endl;
		else if(ct==1)
			outfile<<"Case #"<<t+1<<": "<<cardN<<endl;
		else
			outfile<<"Case #"<<t+1<<": Bad magician!"<<endl;		
	}
	infile.close();
	outfile.close();
	clock_t t2 = clock();
	cout<<"Total time used "<<(t2-t1)/CLOCKS_PER_SEC<<"s"<<endl;
	cin.get();
    return 0;
}
