
#include <stdio.h>
#include <string>

struct Problem
{
	int N;
	int R, P, S;
	void Load()
	{
		scanf("%d %d %d %d", &N,&R,&P,&S);
	}
};

struct Answer
{
	std::string s;
	void Print(int id)
	{
		printf("Case #%d: %s\n", id, s.c_str());
	}
};

class Solver
{
	static const int MAX_N = 12;
	struct MatchPattern
	{
		int winner;
		int win4winner;
		int lose4winner;
	};
	MatchPattern match_pattern[MAX_N+1];
	void SetAnswer(Answer &a, int N, char win)
	{
		a.s = CreateString(win, N);
	}
	std::string CreateSingleString(char c)
	{
		switch (c)
		{
		case 'R':
			return "RS";
		case 'P':
			return "PR";
		case 'S':
			return "PS";
		}
		return "";
	}
	std::string CreateString(char c, int n)
	{
		if (n == 1)
		{
			return CreateSingleString(c);
		}
		std::string s = CreateSingleString(c);
		std::string s0 = CreateString(s[0], n - 1);
		std::string s1 = CreateString(s[1], n - 1);
		if (s0 < s1)
			return s0 + s1;
		return s1 + s0;
	}
public:
	Solver()
	{
		match_pattern[0].winner = 1;
		match_pattern[0].win4winner = 0;
		match_pattern[0].lose4winner = 0;
		for (int i = 0; i < MAX_N; i++)
		{
			match_pattern[i + 1].winner = match_pattern[i].winner + match_pattern[i].win4winner;
			match_pattern[i + 1].win4winner = match_pattern[i].win4winner + match_pattern[i].lose4winner;
			match_pattern[i + 1].lose4winner = match_pattern[i].lose4winner + match_pattern[i].winner;
		}
	}
	Answer solve(const Problem* p)
	{
		Answer a;
		if (p->N > MAX_N)
			printf("ERROR!\n");
		MatchPattern m = match_pattern[p->N];
		if ((m.winner == p->R) && (m.win4winner == p->P) && (m.lose4winner == p->S))
			SetAnswer(a, p->N, 'R');
		else if ((m.winner == p->P) && (m.win4winner == p->S) && (m.lose4winner == p->R))
			SetAnswer(a, p->N, 'P');
		else if ((m.winner == p->S) && (m.win4winner == p->R) && (m.lose4winner == p->P))
			SetAnswer(a, p->N, 'S');
		else
			a.s = "IMPOSSIBLE";
		return a;
	}
};


int main(int argc, char* argv[])
{

	int num;
	scanf("%d", &num);
	Solver solver;

	for (int i = 1; i < num + 1; i++)
	{
		Problem p;
		Answer a;
		p.Load();
		a = solver.solve(&p);
		a.Print(i);
	}

	return 0;
}

