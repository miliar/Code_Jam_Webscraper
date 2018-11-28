#include <fstream>
#include <iostream>
#include <vector>

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

string remove(string mainstr, string digit)
{
	int i=0;
	while (i< mainstr.size())
	//for (int i=0; i<mainstr.size(); i++)
	{
		for (int j=0; j< digit.size(); j++)
			if (mainstr[i]==digit[j])
			{
				//cout << "before: " << mainstr << " " <<  digit << endl;
				digit=digit.substr(0,j)+digit.substr(j+1);
				mainstr=mainstr.substr(0,i)+mainstr.substr(i+1);
				i--;
			}	
		i++;
	}

	return mainstr;
}

bool found_and_removed(string & badphone, string indicator, int digit, string representation, vector<int> & digits)
{
	if (badphone.find(indicator)!=string::npos)
        {
                digits.push_back(digit);
                badphone = remove(badphone,representation);
		return true;
        }
	else
		return false;
}

vector<int> GetPhone(string badPhone)
{
	vector<int> digits;
	//cout << badPhone << endl;
	while (found_and_removed(badPhone, "Z", 0, "ZERO", digits))
	{
	}
	while (found_and_removed(badPhone, "W", 2, "TWO", digits))
        {
        }
	while (found_and_removed(badPhone, "U", 4, "FOUR", digits))
        {
        }
	while (found_and_removed(badPhone, "X", 6, "SIX", digits))
        {
        }
	while (found_and_removed(badPhone, "G", 8, "EIGHT", digits))
        {
        }
	while (found_and_removed(badPhone, "S", 7, "SEVEN", digits))
        {
        }
	while (found_and_removed(badPhone, "V", 5, "FIVE", digits))
        {
        }
	while (found_and_removed(badPhone, "I", 9, "NINE", digits))
        {
        }
	while (found_and_removed(badPhone, "N", 1, "ONE", digits))
        {
        }
	while (found_and_removed(badPhone, "T", 3, "THREE", digits))
        {
        }
	
	sort(digits.begin(), digits.end());	
	return digits;
}

int main(int argc, char** argv)
{
        if (argc!=4)
        {
                cout << "Params: 0 inputFilePath outputFilePath \n";
        }

        ifstream inf;
        inf.open(argv[2]);
        ofstream outf;
        outf.open(argv[3]);

        int n=0;
        string line;
        getline(inf,line);
        n = atoi(line.c_str());

	//cout << "n: " << n << endl;
        for (int i=0; i<n; i++)
        {
		//cout << i << endl;
                getline(inf,line);

		vector<int> x = GetPhone(line);
        	outf << "Case #" << i+1 <<": ";
		//cout << "x.size:" << x.size() << endl;
		for  (int j=0; j< x.size(); j++)
                	outf << x[j] ;
                outf << endl;
        }

	//cout << "Hi there!" << endl;
        outf.close();
        inf.close();
}




