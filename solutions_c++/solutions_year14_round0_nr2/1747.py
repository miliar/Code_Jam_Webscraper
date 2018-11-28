#define _CRT_SECURE_NO_WARNINGS
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

double C, F, X;

int main() {
	clock_t t1 = clock();
	//ifstream infile("test.txt");
    //ifstream infile("B-small-attempt0.in");
	ifstream infile("B-large.in");
	//ofstream outfile("B.out");
	FILE * pFile;
	pFile = fopen ("B-large.out","w");

	int T;
	string instr;
	getline(infile, instr);
	T = stoi(instr);
	cout<<T<<endl;

	for(int t=0; t!=T; t++){
		getline(infile, instr);
		//cout<<instr<<endl;
		string item;
		stringstream sstr = stringstream(instr);
		for(int i=0; i!=3; i++){
			getline(sstr, item, ' ');
			switch(i){
			case 0: stringstream(item)>>C; break;
			case 1: stringstream(item)>>F; break;
			case 2: stringstream(item)>>X; break;
			}
		}
		//cout<<C<<" "<<F<<" "<<X<<endl;
		//printf("Case %02d, C=%9.5f, F=%9.5f, X=%9.5f\n",t+1, C, F, X);
		
		double tm=0.0, rate = 2.0;
		while( (X-C)/rate > X/(rate+F)){
			tm += C/rate;
			rate += F;
		}
		tm += X/rate;
		//cout<<tm<<endl;
		//printf( "Case #%d: %.7f\n",t+1, tm);
		fprintf (pFile, "Case #%d: %.7f\n",t+1, tm);	
	}
	infile.close();
	fclose (pFile);
	clock_t t2 = clock();
	cout<<"Total time used "<<(t2-t1)/CLOCKS_PER_SEC<<"s"<<endl;
	cin.get();
    return 0;
}
