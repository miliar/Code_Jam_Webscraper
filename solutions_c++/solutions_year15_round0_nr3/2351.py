#include <iostream>
#include <string>
#include <vector>

unsigned minus = 0;

char mul(char a, char b)
{
	switch(a)
	{
	case 'i':
		{
			switch(b)
			{
			case 'i':	{++minus; return '1';}
			case 'j':	return 'k';
			case 'k':	{++minus; return 'j';}
			}
		}
		break;
	case 'j':
		{
			switch(b)
			{
			case 'i':	{++minus; return 'k';}
			case 'j':	{++minus; return '1';}
			case 'k':	return 'i';
			}
		}
		break;
	case 'k':
		{
			switch(b)
			{
			case 'i':	return 'j';
			case 'j':	{++minus; return 'i';}
			case 'k':	{++minus; return '1';}
			}
		}
		break;
	}
}

bool solve(std::string S)
{
	unsigned pos = 0;
	char T[4] = "ijk";
	
	//std::cout << '"' << S << '"' << std::endl;
	minus = 0;
	while(S.size() > 3 && pos < 4)
	{
		while(pos < 4) { if(S[pos] == T[pos]) ++pos; else break; }
		
		if(pos+1 < S.size())
		{
			char c = mul(S[pos], S[pos+1]);
			S.erase(pos, 2);
			if(c != '1') S.insert(pos, 1, c);
		}
		else break;
		//std::cout << '"' << S << '"' << std::endl;
	}
	//std::cout << '"' << S << '"' << std::endl;
	
	return (S == "ijk") && ((minus & 1) == 0);
}

int main()
{
	unsigned T;
	std::cin >> T;
	
	for(unsigned t=0; t<T; ++t)
	{
		unsigned L, X;
		std::cin >> L >> X;
		
		std::cout << "Case #" << (t+1) << ": ";
		
		std::string S(""), s;
		std::cin >> s;
		for(unsigned x=0; x<X; ++x) S += s;
		
		if(L == 1 || L*X < 3)
			std::cout << "NO" << std::endl;
		else
			std::cout << (solve(S) ? "YES" : "NO") << std::endl;
	}
	
	return 0;
}
