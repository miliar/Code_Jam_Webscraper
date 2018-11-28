
#include<vector>
#include<fstream>
#include<iostream>
#include<string>
using namespace std;

int main(int argc, char* argv[])
{
	string inputfilename="input.txt";
	string outputfilename="output.txt";
	string testname="test.txt";
	ifstream infile(inputfilename);
	ofstream OF(outputfilename);
	ofstream TEST(testname);
	int T;
	infile>>T;

	for(int icase=0;icase<T;icase++){
		vector<int> s;
		int smax=0;
		string sbuf;
		char cbuf[1];
		infile>>smax>>sbuf;

		for(int i=0;i<=smax;i++){
			cbuf[0]=sbuf[i];
			s.push_back(atoi(cbuf));		
			
		}
	
		int standing_count=0;
		int friends_needed=0;
		for(int i=0;i<s.size();i++){
			if(standing_count<i){
				friends_needed+=i-standing_count;
				standing_count+=i-standing_count;
			}
			standing_count+=s[i];
			
		}
	
	
	
		OF<<"Case #"<<icase+1<<": "<<friends_needed<<endl;
		TEST<<icase+1<<": ";
		for(int i=0;i<s.size();i++){
			TEST<<s[i];
		}
		TEST<<" : "<<friends_needed<<endl;
	}

		

	infile.close();
	OF.close();
	TEST.close();
	return 0;
}

