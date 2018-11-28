#include <fstream>
#include <string>
#include <vector>
using namespace std;

int functx(string& input, int count)
{
	if(input.find('-') == std::string::npos) return count;
	if(input.find('+') == std::string::npos) return count+1;
	else{
		int pos = input.find('+');
		int post = input.find('-');
		if(pos == 0 && input.back()=='+'){
			string x = input.substr(0, post);
			input.erase(input.begin(),input.begin()+post);
			string a(x.length(),'+');
			input+=a;
			return functx(input, count+1);
		}
		else if(pos == 0 && input.back() == '-'){
			string x = input.substr(0, post);
			input.erase(input.begin(),input.begin()+post);
			string a(x.length(),'-');
			input+=a;
			return functx(input, count+1);
		}
		else if(post == 0 && input.back() == '-'){
			string x = input.substr(0, pos);
			input.erase(input.begin(),input.begin()+pos);
			string a(x.length(),'-');
			input+=a;
			return functx(input, count+1);
		}
		else{
			string x = input.substr(0, pos);
			input.erase(input.begin(),input.begin()+pos);
			string a(x.length(),'+');
			input+=a;
			return functx(input, count+1);
		}
	}
}

int functy(string& input,string& inputx, int count)
{
	if(input == inputx && count !=0) return functx(input, count);
	if(input.find('-') == std::string::npos) return count;
	if(input.find('+') == std::string::npos) return count+1;
	else
	{
		int pos = input.find('+');
		int post = input.find('-');
		if (post<pos){
			if(pos == 1){
				input[0]='+';
				return functy(input,inputx,count+1);
			}
			string x = input.substr(0, pos);
			input.erase(input.begin(),input.begin()+pos);
			string a(x.length(),'+');
			input+=a;
			return functy(input,inputx, count+1);
		}
		else{
			if(post==1){
				input[0]='-';
				return functy(input,inputx, count+1);
			}
			string x = input.substr(0,post);
			input.erase(input.begin(),input.begin()+post);
			string a(x.length(),'-');
			input+=a;
			return functy(input, inputx, count+1);
		}
	}
}

int main()
{
	int T,x=1;
	string input;
	vector<int> results;
	ifstream filex;
	ofstream filx;
	filex.open("B-small-attempt5.in");
	filx.open("B-small-attempt5.out");
	filex>>T;
	for(int i=0; i!=T; i++)
	{
		filex>>input;
		if(input.find('-')==std::string::npos) results.push_back(0);
		else
			results.push_back(functx(input,0));
	}
	for(vector<int>::iterator it = results.begin(); it!=results.end();it++)
	{
		if(it == results.end()-1)
			filx<<"Case #"<<x<<": "<<*it;
		else
			filx<<"Case #"<<x<<": "<<*it<<endl;
		x++;
	}
	return 0;
}