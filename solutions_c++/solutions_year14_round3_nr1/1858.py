#include<iostream>
#include<vector>
#include <fstream>
#include <sstream>
#include <algorithm> 
#include <string>
using namespace std;

template<typename T>
struct Mat{
	vector<T> data;
	int row, col;

	Mat(int row, int col): row(row),col(col){
		data.resize(row*col);
	}
	Mat(int row, int col, const T& val): row(row),col(col){
		data.resize(row*col,val);
	}

	inline void  set(int i, int j, T val){
		data[i*col+j]=val;
	}

	T& operator()(int i, int j){
		return data[i*col+j];
	}
	inline const T& operator()(int i, int j)const {
		return data[i*col+j];
	}

	Mat transpose(){
		Mat out(col, row);
		for(int i=0; i<row;i++)
			for (int j =0;j<col;j++)
				out(j,i)=data[i*col+j];
		return out;
	}
};

template<typename T>
ostream& operator<<(ostream& out,  const Mat<T>& M ){
	for(int i=0; i<M.row;i++){
		for (int j =0;j<M.col;j++){
			out<<M(i,j)<<" ";		
		}
		out<<endl;
	}
	return out;
}

struct Pair{
	int id;
	int value;
};

bool smaller(Pair& i, Pair& j){	return i.value<j.value;}


int main() {
	ifstream input("../A-small-attempt1.in");
	//ifstream input("../A-large.in");


	if(!input.is_open()) {
		cerr<< "problem"<<endl;
	}
	
	int number;
	input>>number;

	vector<int> result(number+1); 
	for(int it=1;it<= number; it++){
		//loading
		int P, Q;
		string s,s2;
		std::getline(input,s,'/');
		std::getline(input,s2);
		cout<<s<<endl;
		cout<<s2;

		std::stringstream f;
		f<<s;
		f>>P;
		f.clear();
		f<<s2;
		f>>Q;
		//code
		while (P%2==0 && Q%2==0){
			P/=2;
			Q/=2;
		}
		int Q2=Q;
		int limi=0;
	    while (Q2%2==0){
			Q2/=2;
			limi++;
		}
		if (Q2!=1 || limi==0){
			result[it]=0; 
			continue;
		}
		if (P==Q){
			result[it]=1; 
			continue;
		}

		int gene=1;
		int fac=2;
		while( gene<=limi && (float)P/Q < 1.0/fac){
			fac*=2;
			gene++;
		}
		
		//result
		
		result[it]=gene;
	}

	
	//==============output
	ofstream output("../answer.txt");
	for(int i=1;i<=number;i++)
	{
		output<<"Case #"<<i<<": ";
		if (result[i]==0) output<<"impossible";
		else		output<< result[i];
		output<<endl;
	}
	output.close();

	return 0;
}