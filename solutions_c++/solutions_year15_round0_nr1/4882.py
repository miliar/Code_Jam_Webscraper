#include<iostream>
#include<fstream>
#include<string>
#include<string.h>
#include<vector>
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
class ShynessDataSet :public DataSet {

	public:
	string in;
	int length;
       
	public:

	void read(ifstream& ifs) {
		ifs>>length>>in;
		length++;
	}
	void setIn(string in) {
		this->in=in;
	}

	string getIn(){ return in;}

};

class Algo {

	public:

		virtual void execute(ShynessDataSet data,int caseNo)=0;

};


class ShynessAlgo:public Algo {

	public:
            
         ShynessAlgo() {
               
		}
	 virtual void execute(ShynessDataSet element,int caseNo){
		const char* str=element.in.c_str();
		long reCount=0;
		long reqFriends=0;
		for(int i=0;i<element.length;i++)
		{
			int currentPos=str[i]-48;
			if(reCount< i && currentPos) {
				reqFriends+=(i-reCount);
				reCount=i;
			}
			reCount+=currentPos;
		}
		cout<<"Case #"<<caseNo<<": "<<reqFriends<<endl;		
	 	}

	 };

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
		 executor.execute<ShynessDataSet,ShynessAlgo>();
		 return 0;
	 }
