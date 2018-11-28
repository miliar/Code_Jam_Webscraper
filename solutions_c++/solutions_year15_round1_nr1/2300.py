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
class ProbADataSet :public DataSet {

	public:///Data
	int  in[1001];
	int length;
       
	public:

	void read(ifstream& ifs) {
		ifs>>length;
		for(int i=0;i<length;i++)
		ifs>>in[i];
	}

};

class Algo {

	public:

		virtual void execute(ProbADataSet data,int caseNo)=0;

};


class ProbAAlgo:public Algo {

	public:
            
         ProbAAlgo() {
               
		}
	 virtual void execute(ProbADataSet element,int caseNo){
		int count=0;
		int prev=element.in[0];
		int maxDiff=0;
		for(int i=1;i<element.length;i++) {
		if(prev > element.in[i])
		{
		int diff=(prev-element.in[i]);
		 if(maxDiff<diff) maxDiff=diff;
		 count+=diff;
		}
		prev=element.in[i];
		}
		//cout<<"max Diff"<<maxDiff<<endl;
		int meth2=0;
		//int prev=element.in[0];
		//meth2=prev>maxDiff?maxDiff:prev;
		for(int i=0;i<element.length-1;i++) {
		int a=element.in[i];
		if(a>=maxDiff) {
			meth2+=maxDiff;
		}else{
		meth2+=a;	
		} 
		
		}
			///Logic
		cout<<"Case #"<<caseNo<<": "<<count<<" "<<meth2<<endl;		
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
		 executor.execute<ProbADataSet,ProbAAlgo>();
		 return 0;
	 }
