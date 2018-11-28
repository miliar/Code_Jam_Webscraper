#include <bits/stdc++.h>

using namespace std;
#define LL long long
#define FORI(A,B,C) for(int I=(A);I<=(B); I++)
#define FORLL(A,B,C) for(L I=(A);I<=(B); I++)

string fun(string str){
	string res="";
	res+=str[0];
	for (int i=1;i<str.size();i++){
		if (str[i]>=res[0]){
			res=str[i]+res;
		}else{
			res+=str[i];
		}
	}
	return res;
}

LL funv(vector<LL> num){
	return -1;
}

int main() {
    ifstream ifile;
    ofstream ofile;
    ifile.open("Input.txt");
    ofile.open("Output.txt");

    int CaseIdx,TotalCase;
    string line;
    getline(ifile,line);
    stringstream ss(line);
    ss>>TotalCase;

    for (CaseIdx = 1; CaseIdx<=TotalCase; CaseIdx++)
    {
//  begin of code
  //  1. prepare data for current test case
    	LL A,B,C;
    	LL N;
    	string str;
    	vector<LL> nums;

		string line;
		{
			getline(ifile,line);
			stringstream ss(line);
			ss>>str;
		}

  //  2. data_pre_processing if possible. (significantly reduced time/space complextity


  //  3. data_processing to get the result
		string res = fun(str);
		//int res = funv(nums);

  //  4. Output results;
		string caseResult="";
		caseResult += res;

    	cout<<"Case #"<<CaseIdx<<": "<<caseResult<<endl;
    	ofile<<"Case #"<<CaseIdx<<": "<<caseResult<<endl;

// end of code
    }


    ifile.close();
    ofile.close();
	return 0;
}

