#include <stdio.h>
#include <fstream>
#include <vector>
#include <string>
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
	*length = numbers_in_line.size();
	return numbers_in_line;
}
// [0]

class TicTacToeTomek
{
	string file_name, file_content;
	long file_length;
	vector<string> content_in_lines;
	ifstream ifs;
public:
	TicTacToeTomek(string file_name): file_name(file_name)
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
	string getCase(int case_no)
	{
		vector<string> case_lines;
		int new_line_flag = 0;
		string case_line;
		int t_x = -1, t_y = -1, dots_finder;
		bool there_are_dots = false;
		for (int i = 0; i < 4; i++)
		{
			//case_line.append(getLine(i+((case_no)*4)+1+(new_line_flag/4)));
			case_line.append(getLine(i+(case_no*4)+1));
			case_lines.push_back(case_line);
			new_line_flag++;
			t_y = case_line.find_first_of('T');
			dots_finder = case_line.find_first_of('.');
			if (t_y != std::string::npos)
				t_x = i;
			if (dots_finder != std::string::npos)
				there_are_dots = true;
			case_line = "";
		}

		int ti1 = 0, tj1 = 0
		,	ti2 = 3, tj2 = 0
		,	ti3 = 3, tj3 = 3;

		int c1_x = 0, c1_o = 0, c1_dot = 0;
		int c2_x = 0, c2_o = 0, c2_dot = 0;
		int c3_x = 0, c3_o = 0, c3_dot = 0;
		int c4_x = 0, c4_o = 0, c4_dot = 0;

		if(case_lines[0][0] == 'X' || case_lines[0][0] == 'T') c3_x++;
		if(case_lines[0][0] == 'O' || case_lines[0][0] == 'T') c3_o++;
		if(case_lines[0][0] == '.') c3_dot++;
		if(case_lines[1][1] == 'X' || case_lines[1][1] == 'T') c3_x++;
		if(case_lines[1][1] == 'O' || case_lines[1][1] == 'T') c3_o++;
		if(case_lines[1][1] == '.') c3_dot++;
		if(case_lines[2][2] == 'X' || case_lines[2][2] == 'T') c3_x++;
		if(case_lines[2][2] == 'O' || case_lines[2][2] == 'T') c3_o++;
		if(case_lines[2][2] == '.') c3_dot++;
		if(case_lines[3][3] == 'X' || case_lines[3][3] == 'T') c3_x++;
		if(case_lines[3][3] == 'O' || case_lines[3][3] == 'T') c3_o++;
		if(case_lines[3][3] == '.') c3_dot++;

		if(c3_x == 4) return "X won";
		else if(c3_o == 4) return "O won";


		if(case_lines[0][3] == 'X' || case_lines[0][3] == 'T') c4_x++;
		if(case_lines[0][3] == 'O' || case_lines[0][3] == 'T') c4_o++;
		if(case_lines[0][3] == '.') c4_dot++;
		if(case_lines[1][2] == 'X' || case_lines[1][2] == 'T') c4_x++;
		if(case_lines[1][2] == 'O' || case_lines[1][2] == 'T') c4_o++;
		if(case_lines[1][2] == '.') c4_dot++;
		if(case_lines[2][1] == 'X' || case_lines[2][1] == 'T') c4_x++;
		if(case_lines[2][1] == 'O' || case_lines[2][1] == 'T') c4_o++;
		if(case_lines[2][1] == '.') c4_dot++;
		if(case_lines[3][0] == 'X' || case_lines[3][0] == 'T') c4_x++;
		if(case_lines[3][0] == 'O' || case_lines[3][0] == 'T') c4_o++;
		if(case_lines[3][0] == '.') c4_dot++;

		if(c4_x == 4) return "X won";
		else if(c4_o == 4) return "O won";

		for (int i = 0; i < 4; i++)
		{
			c1_x = 0;
			c1_o = 0;
			c1_dot = 0;
			
			c2_x = 0;
			c2_o = 0;
			c2_dot = 0;
			for (int j = 0; j < 4; j++)
			{	
				if(case_lines[i][j] == 'X' || case_lines[i][j] == 'T') c1_x++;
				if(case_lines[i][j] == 'O' || case_lines[i][j] == 'T') c1_o++;
				if(case_lines[i][j] == '.') c1_dot++;

				if(c1_x == 4) return "X won";
				else if(c1_o == 4) return "O won";

				if(case_lines[j][i] == 'X' || case_lines[j][i] == 'T') c2_x++;
				if(case_lines[j][i] == 'O' || case_lines[j][i] == 'T') c2_o++;
				if(case_lines[j][i] == '.') c2_dot++;

				if(c2_x == 4) return "X won";
				else if(c2_o == 4) return "O won";
			}
		}
		if (there_are_dots)
			return "Game has not completed";
		else
			return "Draw";
	}
	string retrieveAllText(){ return file_content; }
};

int main (int argc, char **argv)
{
//	int cases;
	TicTacToeTomek rws("A-large.in");
	rws.tokenizeToLines(); 
	int cases = string2int(rws.getLine(0));

	ofstream outfile;
	outfile.open("A-large-out.outf", ios::out);
	for (int i = 0; i < cases; i++)
		outfile << "Case #" << i+1 << ": " << rws.getCase(i).c_str() << endl;
	
	//outfile << "whichever" << endl;
	outfile.close();
	return 0;
}