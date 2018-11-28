#include<fstream>
#include<vector>

struct _case
{
	int x;
	int r;
	int c;
};

typedef std::vector<std::string> vs;
std::vector<_case> cases;
int n_cases;

vs results;

std::string solve(_case c);

int main()
{
	//input
	std::ifstream input;
	input.open("input.in");
	if(!input.eof())
	{
		input>>n_cases;
		for(int i = 0; i < n_cases; i++)
		{
			_case this_case;
			input>>this_case.x;
			input>>this_case.r;
			input>>this_case.c;
			
			cases.push_back(this_case);
		}
	}
	input.close();

	//solve
	for(int i = 0; i < cases.size(); i++) results.push_back(solve(cases[i]));

	//print output
	std::ofstream output;
	output.open("output.txt");
	for(int i = 0; i < results.size(); i++)
	{
		output<<"Case #"<<i+1<<": "<<results[i]<<std::endl;
	}
	output.close();
}

std::string solve(_case c)
{
	switch(c.x)
	{
		case 1:
			return "GABRIEL";
			break;
		case 2:
			{
				if((c.r * c.c) % 2 == 0) return "GABRIEL";
				else return "RICHARD";
			} break;
		case 3:
			{
				if((c.r == 3 && c.c > 1) || (c.c == 3 && c.r > 1)) return "GABRIEL";
				else return "RICHARD";
			} break;
		case 4:
			{
				if((c.r == 4 && c.c > 2) || (c.c == 4 && c.r > 2)) return "GABRIEL";
				else return "RICHARD";
			} break;
	}
}
