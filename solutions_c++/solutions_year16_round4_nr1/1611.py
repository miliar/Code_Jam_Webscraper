#include <bits/stdc++.h>

using namespace std;
#define LL long long
#define FORI(A,B,C) for(int I=(A);I<=(B); I++)
#define FORLL(A,B,C) for(LL I=(A);I<=(B); I++)
#define VLL vector<LL>
#define VVLL vector<vector<LL>>
#define VI vector<int>
#define VVI vector<vector<int>>

#define showv(A) for(auto &x:A){cout<<x<<" ";}cout<<endl;

bool check(string s){
	int sz=s.size();
	if (sz==1) return true;
	if (sz==2) return s[0]!=s[1];
	string s1=s.substr(0,sz/2),s2=s.substr(sz/2);
	string s3 =s1,s4=s2;
	sort(s3.begin(),s3.end());sort(s4.begin(),s4.end());
	return s3!=s4 && check(s1) && check(s2);
}

string fun(LL N, LL R, LL P, LL S){
	string temp1(R,'R'),temp2(P,'P'),temp3(S,'S'),temp,temp0;
	temp=temp2+temp1+temp3;
	temp0=temp;
	do{
		//cout<<temp<<endl;
		if (check(temp)) {
			return temp;
		}
		next_permutation(temp.begin(),temp.end());
	}while ( temp!=temp0);
    return "IMPOSSIBLE";
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
    	LL R,P,S;
    	LL N;
    	vector<LL> nums;

		string line;
		{getline(ifile,line);stringstream ss(line);ss>>N>>R>>P>>S;}


  //  2. data_pre_processing if possible. (significantly reduced time/space complextity

  //  3. data_processing to get the result
		string res = fun(N,R,P,S);


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
