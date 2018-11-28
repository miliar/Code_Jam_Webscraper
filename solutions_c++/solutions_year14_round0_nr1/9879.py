#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

void input(ifstream& infile, 
		   stringstream& stream, 
		   int *row, int (*array)[4][4]){
	string line, word;
	for(int i = 0; i < 2; i++){
		getline(infile, line);
		stream.clear();
		stream.str(line);
		stream>>row[i];
		for(int j = 0; j < 4; j++){
			getline(infile, line);
			stream.clear();
			stream.str(line);
			for(int k = 0; k < 4; k++){
				stream>>array[i][j][k];
			}
		}
	}
}

void judge(int *a, int *b, int no, ofstream& outfile){
	int count = 0;
	int val = -1;
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(a[i] == b[j]){
				count++;
				val = a[i];
			}
		}
	}
	cout<<"Case #"<<no<<": ";
	outfile<<"Case #"<<no<<": ";
	if(count == 0){
		cout<<"Volunteer cheated!"<<endl;
		outfile<<"Volunteer cheated!"<<endl;
	}else if(count == 1){
		cout<<val<<endl;
		outfile<<val<<endl;
	}else{
		cout<<"Bad magician!"<<endl;
		outfile<<"Bad magician!"<<endl;
	}
}
void output(int *row, int(*array)[4][4]){
	for(int i = 0; i < 2; i++){
		cout<<row[i]<<endl;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				cout<<array[i][j][k]<<" ";
			}
			cout<<endl;
		}
	}
}
int main(int argc, char const *argv[])
{
	// string inputfile = "test.in";
	// string outputfile = "test.out";
	string inputfile = "A-small-attempt0.in";
	string outputfile = "A-small-attempt0.out";
	// string inputfile = "B-large-practice.in";
	// string outputfile = "B-large-practice.out";
	ifstream infile(inputfile.c_str());
	ofstream outfile(outputfile.c_str());

	stringstream stream;
	string line;
	int row[2];
	int array[2][4][4];
	getline(infile, line);
	stream.str(line);
	int T;
	stream>>T;
	//cout<<T<<endl;
	for(int no = 0; no < T; no++){
		input(infile, stream, row, array);
		//output(row, array);
		judge(array[0][row[0]-1], array[1][row[1]-1], no+1, outfile);
	}
	return 0;
}