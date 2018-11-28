#include <fstream>
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

void Tokenize(vector<string> & tokens, string line)
{
        string token="";
        string oneCharString = " ";
        for (int i=0; i< line.size(); i++)
                if (line[i]==' ')
                {
                        tokens.push_back(token);
                        token="";
                }
                else
                {
                        oneCharString[0] = line[i];
                        token += oneCharString;
                }
        if (token!= "")
                tokens.push_back(token);
}

string GetLast(string word)
{
	string ans = "";
	string oneCharStr = " ";
	int n=word.size();
	oneCharStr[0]=word[0];
	ans = oneCharStr;
	for (int i=1; i<n; i++)
	{
		oneCharStr[0]=word[i];
		if (word[i]>=ans[0])
			ans=oneCharStr+ans;
		else
			ans= ans+oneCharStr;
			
	}
	return ans;
}

int main(int argc, char** argv)
{
	if (argc!=4)
	{
		//cout << "Params: 0 inputFilePath outputFilePath \n"; 
	}

	ifstream inf;
	inf.open(argv[2]);
	ofstream outf;
	outf.open(argv[3]);

	int n=0;
	string line;
	getline(inf,line);
	n = atoi(line.c_str());
	
	for (int i=0; i<n; i++)
	{
		getline(inf,line);
		string answer = GetLast(line);
		outf << "Case #" << i+1 <<": " << answer << endl;
	}	

	outf.close();
	inf.close();
}
