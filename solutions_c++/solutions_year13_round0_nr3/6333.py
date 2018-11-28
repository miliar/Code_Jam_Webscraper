
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <stdint.h>

using namespace std;

#define Log(x) std::cerr << x
#define Error(x) std::cerr << x; return false

template <typename T>
std::string Vector2String(const std::vector<T>& v)
{
	std::stringstream ss;
	std::vector<T>::const_iterator ite = v.begin();
	for(; ite != v.end(); ++ite)
	{
		ss << *ite << ", ";
	}
	return ss.str();
}

typedef uint64_t BIGNUM;

std::map<BIGNUM, BIGNUM> GetSquareList(const BIGNUM end)
{
	std::map<BIGNUM, BIGNUM> result;
	for(BIGNUM i = 0; i <= end; ++i)
	{
		BIGNUM s = i * i;
		if(s > end)
		{
			break;
		}
		result.insert(std::pair<BIGNUM, BIGNUM>(s, i));
	}
	return result;
}

bool IsFair(const BIGNUM& n)
{
	if(n < 10)
	{
		return true;
	}
	std::stringstream ss;
	ss << n;
	std::string s = ss.str();

	std::string rhS = s.substr(0, s.size() / 2);
	std::string lhS;
	if((s.size() % 2) == 0)
	{
		lhS = s.substr(s.size() / 2, s.size());
	}
	else
	{
		lhS = s.substr(s.size() / 2 + 1, s.size());
	}
	std::string reverse_lhS = lhS;
	std::reverse(reverse_lhS.begin(), reverse_lhS.end());

	return rhS.compare(reverse_lhS) == 0;
}

std::vector<BIGNUM> ComputeSquareFairList(std::map<BIGNUM, BIGNUM>& square_list)
{
	std::vector<BIGNUM> result;
	std::map<BIGNUM, BIGNUM>::const_iterator s_ite = square_list.begin();
	for(; s_ite != square_list.end(); ++s_ite)
	{
		//std::cout << s_ite->first << "(" << s_ite->second << "^2)" << std::endl;
		BIGNUM target = s_ite->first;
		if(!IsFair(target) || !IsFair(s_ite->second))
		{
			continue;
		}

		//std::cout << target << "(" << s_ite->second << "^2)" << std::endl;
		result.push_back(target);
	}
	return result;
}

class Interval
{
public:
	BIGNUM m_Start;
	BIGNUM m_End;
	std::vector<BIGNUM>& m_AnswerList;
	Interval(const BIGNUM start, const BIGNUM end, std::vector<BIGNUM>& answer_list)
	: m_Start(start), m_End(end)
	, m_AnswerList(answer_list)
	{};

	std::string GetDescription()
	{
		std::stringstream ss;
		ss << "start: " << m_Start << " end: " << m_End << std::endl;

				
		return ss.str();
	}

	BIGNUM Solve()
	{
		BIGNUM ans = 0;
		std::vector<BIGNUM>::const_iterator ite = m_AnswerList.begin();
		for(; ite != m_AnswerList.end() && *ite <= m_End; ++ite)
		{
			if(*ite >= m_Start)
			{
				ans++;
			}
		}
		return ans;
	}
};

class ProblemC
{
public:
	ProblemC()
	{
	}

	bool ReadProblem(std::istream& input, std::vector<Interval>& out_problem_list, std::vector<BIGNUM>& square_fair_list)
	{
		std::string buf;

		if( ! std::getline(input, buf) )
		{
			Error("一行目の読み込みに失敗");
		}
		int n = atoi(buf.c_str());
		if( n <= 0 )
		{
			Error("一行目が数値に変換しても 0 でした。");
		}

		for(int i = 0; i < n; ++i)
		{
			if( ! std::getline(input, buf) )
			{
				Error("問題の読み込みに失敗しました。");
			}
			BIGNUM start;
			BIGNUM end;
			if( sscanf(buf.c_str(), "%llu %llu", &start, &end) != 2)
			{
				Error("問題に数字が2つはありませんでした。");
			}

			out_problem_list.push_back(Interval(start, end, square_fair_list));
		}
		return true;
	}

	bool Main()
	{
		std::vector<Interval> problem_list;
		std::vector<BIGNUM> square_fair_list;
		BIGNUM max = 0;
		if( ! ReadProblem(std::cin, problem_list, square_fair_list) )
		{
			return false;
		}
		std::vector<Interval>::iterator ite = problem_list.begin();
		for(; ite != problem_list.end(); ++ite)
		{
			if(max < ite->m_End)
			{
				max = ite->m_End;
			}
		}

		square_fair_list = ComputeSquareFairList(GetSquareList(max));
		ite = problem_list.begin();
		int i = 1;
		for(; ite != problem_list.end(); ++ite, ++i)
		{
			//std::cout << ite->GetDescription();
			std::cout << "Case #" << i << ": " << ite->Solve() << std::endl;
		}

		return true;
	}
};



int main(int argc, char *argv[])
{
	ProblemC p;
	p.Main();
	return 0;
}
