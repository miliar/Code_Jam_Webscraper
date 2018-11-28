#include<iostream>
#include<fstream>
#include<string>
#include<string.h>
#include<vector>
#include <stdlib.h>   
using namespace std;

template <typename T> 
class TestCase {
	int count;
	vector<T> dataset;
	public :
	void setCount(int count){
		this->count=count;
	}

	void add(T element)
	{

		dataset.push_back(element);
	}

	vector<T>& get() {
		return dataset;
	}

	virtual ~TestCase()
	{

	}


};

class DataSet  {
	public :
		virtual void read(ifstream& ifs) =0;

}
;
class DijkstraDataSet :public DataSet {

	public:
	string in;
	int length,times;
       
	public:

	void read(ifstream& ifs) {
		ifs>>length>>times;
		ifs>>in;
	}
	void setIn(string in) {
		this->in=in;
	}

	string getIn(){ return in;}

};

class Algo {

	public:

		virtual void execute(DijkstraDataSet data,int caseNo)=0;

};


class DijkstraAlgo:public Algo {
	static int table[5][5];
	
	public:
            
         DijkstraAlgo() {
               
		}
	 int mul(int i, int j) {
	 // cout<<"("<<i<<","<<j<<")";//<<endl; 		
	  int signI=i/abs(i);
	  int signJ=j/abs(j);
	 // cout<<"=="<<signJ*signI*table[abs(i)][abs(j)]<<endl;
	  return signJ*signI*table[abs(i)][abs(j)];
	}
	
	 virtual void execute(DijkstraDataSet element,int caseNo){
				int checkVal=2;
				int val=1;
				for(int i=0;i<element.times;i++) {
					for(int pos=0;pos<element.length;pos++) {
						val=mul(val,(element.in.c_str()[pos]-103));
						if(val==checkVal) {
							checkVal++;
							val=1;
						}
					}
				}
				if(checkVal==5 && val==1) {
				cout<<"Case #"<<caseNo<<": YES"<<endl;		
				}else {
				cout<<"Case #"<<caseNo<<": NO"<<endl;		
				}
	 }

};
int DijkstraAlgo::table[5][5]={{0,0,0,0,0},{0,1,2,3,4},
	{0,2,-1,4,-3},
	{0,3,-4,-1,2},
	{0,4,3,-2,-1}};
class TestExecutor {
	ifstream ifs;
	string fname;

	public:
	TestExecutor(){
	}
	virtual ~TestExecutor() {
	}
	void setFileName(string name) {
		this->fname=name;
	}
	template<class DataSet, class Algo>
		void execute()	{
			ifs.open (fname.c_str(), std::ifstream::in);
			int count;
			ifs>>count;
#ifdef DEBUG
			cout<<"No of Test Cases"<<count<<endl;
#endif
			int records=0;
			Algo algo;
			while (ifs.good()&& records <count) {
				DataSet element;
				element.read(ifs);
				algo.execute(element,records+1);
				records++;			
			}

			ifs.close();

		}

};


int main (int argc, char* argv[])
{
	TestExecutor executor;
	if(argc >1)
		executor.setFileName(argv[1]);
	else
		executor.setFileName("in.txt");
	executor.execute<DijkstraDataSet,DijkstraAlgo>();
	return 0;
}
