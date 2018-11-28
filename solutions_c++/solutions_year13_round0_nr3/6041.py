#include <stdio.h>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;

#define MAX_LINE_LENGTH 4

// [0] Converters
int string2int(string s)
{
	const char *sc = s.c_str();
	int len = strlen(sc);
	int result = 0;
	for(int i = len-1, mul = 1; i >= 0; i--, mul *= 10)
	{
		int toI = sc[i]-48;
		if (toI >=0 && toI <= 9)
			result += mul*(toI);
		else
			return 0;
	}
	return result;
}
int string2int(char *s)
{
	
	int len = strlen(s);
	int result = 0;
	for(int i = len-1, mul = 1; i >= 0; i--, mul *= 10)
	{
		int toI = s[i]-48;
		if (toI >=0 && toI <= 9)
			result += mul*(toI);
		else
			return 0;
	}
	return result;
}
vector<int> extractNumbers(string s, int *length)
{
	const char *sc = s.c_str();
	int len = strlen(sc);
	char *token = strtok((char*)sc, " \t");
	int i = 0;
	vector<int> numbers_in_line;
	while (token != NULL)
	{
		numbers_in_line.push_back(string2int(token));
		token = strtok(NULL, " \t");
		i++;
	}
	if(length != '\0')
		*length = numbers_in_line.size();
	return numbers_in_line;
}
int pow(int b, int p)
{
	if (p < 0) return 0;
	if (p == 0) return 1;
	return b * pow(b, p - 1);
}
// end of helpers

// converters
bool is_palindrome(long num)
{
	// [1] decimal check
	if (num <= 9) return true;

	int digits_no = 0, mod = 1;
//	long temp = num / mod;
	vector<int> num_digitized;
	while (num >= mod)
	{
		num_digitized.push_back((num%(mod*10))/mod);
		mod *= 10;
	}
	int vec_size = num_digitized.size();
	bool flag = true;
	for (int i = 0, j = vec_size-1; i < vec_size/2; i++, j--)
	{
		if (num_digitized[i] != num_digitized[j]) flag = false;
	}
	if (flag) return true;
	// [1]

	// [2] binary check
	int	comparer = 1;
	int *len = new int;
	*len = 0;
	while (num >= comparer)
	{
		++(*len);
		comparer *= 2;
	}
	
	char *res = new char[*len];
	
	if (num == 1 || num == 0)
	{
		*len = 1;
		char *res = new char[1];
		*res = num;
		return res;
	}

	char dumdum;
	int counter = 0;
	while (num > 0)
	{
		dumdum = num%2;
		res[*len - counter - 1] = dumdum;
		num >>= 1;
		//num /=2;
		++counter;
	}

	
	for (int begin = 0, end = *len-1 ; begin < *len; begin++, end--)
	{
		if (res[begin] != res[end])
			return false;
	}
	return true;
	// [2]
}
bool isPerfectSquare(long input)
{
    long closestRoot = (long) sqrt(input);
    return input == closestRoot * closestRoot;
}

// [0]

class FairSQ
{
	string file_name, file_content;
	long long file_length;
	vector<string> content_in_lines;
	ifstream ifs;
public:
	FairSQ(string file_name): file_name(file_name)
	{
		ifstream ifs;
		ifs.open(file_name.c_str(), ios::in);
		ifs.seekg(0, ifs.beg);
		filebuf *buffer = ifs.rdbuf();
		file_length = buffer->pubseekoff(0,ios::end,ios::in);
		buffer->pubseekpos(0,ios::in);

		char *s=new char[file_length];
		buffer->sgetn(s, file_length);
		file_content.assign(s, file_length);
		ifs.close();

	}
	vector<string> tokenizeToLines()
	{
		vector<string> res;
		string one_sentence = "";
		const char *dummy = file_content.c_str();
		for(int i = 0; i < file_length; i++)
		{
			if(file_content[i] != '\n')
				one_sentence.push_back(dummy[i]);
			else
			{
				if (one_sentence != "")
					res.push_back(one_sentence);
				one_sentence = "";
			}
		}
		if (one_sentence != "")
			res.push_back(one_sentence);
		content_in_lines = res;
		return res;
	}
	string getLine(int lineNo){ return content_in_lines[lineNo]; }
	int getCase(int case_no)
	{
		string case_line = getLine(case_no+1);

		vector<int> case_numbers = extractNumbers(case_line, NULL);
		
		int counter = 0;
		//printf("\nFrom %d to %d:\n", case_numbers[0], case_numbers[1]);
		for(int i = case_numbers[0]; i <= case_numbers[1]; i++)
		{
			if (isPerfectSquare(i) && is_palindrome(i))
			{
				int dumdum = sqrt(i);
				if(is_palindrome(dumdum))
					counter++;
				//printf("%d, ", i);
			}
		}
		return counter;
	}
};

int main (int argc, char **argv)
{
//	int cases;
	FairSQ rws("C-small-attempt2.in");
	rws.tokenizeToLines(); 
	
	int cases = string2int(rws.getLine(0));

	ofstream outfile;
	outfile.open("C-small-attempt-1.outf", ios::out);
	
	for (int i = 0; i < cases; i++)
		outfile << "Case #" << i+1 << ": " << rws.getCase(i) << endl;
	
	outfile.close();
	return 0;
}