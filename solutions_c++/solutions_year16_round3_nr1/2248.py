#include <iostream>
#include <fstream>

int max(int *s, int nb)
{
	int x(0);
	
	for(int i(0); i < nb; i++)
	{
		if(s[i] > x)
		{
			x = s[i];
		}
	}
	
	return x;
}

int find(int *s, int nb, int search)
{
	int x(0);
	for(int i(0); i < nb; i++)
	{
		if(s[i] == search)
		{
			x++;
		}
	}
	return x;
}

int first(int *s, int nb, int search)
{
	int x(0);
	
	for(int i(0); i < nb; i++)
	{
		if(s[i] == search)
		{
			return i;
		}
	}
}

int main()
{
	std::ifstream in("in");
	std::ofstream out("out");
	
	int N(0);
	
	in >> N;
	
	for(int i(0); i < N; i++)
	{
		out << "Case #" << i+1 << ": ";
		
		int I(0);
		
		in >> I;
		
		int *S = new int[I+1];
		
		for(int j(0); j < I; j++)
		{
			in >> S[j];
		}
		S[I] = 0;
		
		int m(max(S, I));
		
		while(m != 0)
		{
			int tmp = find(S, I, m);
			
			if(tmp > 0)
			{
				std::cout << "IT" << std::endl;
				for(int k(0); k < I; k++)
				{
					std::cout << S[k] << " ";
				}
				std::cout << std::endl;
				
				if(tmp%2 == 0)
				{
					int f = first(S, I, m);
				
					out << (char)('A' + f);
					S[f]--;
					
					std::cout << f << " ";
				
					f = first(S, I, m);
				
					out << (char)('A' + f);
					S[f]--;
					std::cout << f << " ";
				}
				else
				{
					int f = first(S, I, m);
				
					out << (char)('A' + f);
					S[f]--;
					std::cout << f << " ";
				}
				
				std::cout << std::endl;
			}
			
			out << ' ';
			
			m = max(S, I);
		}
		
		out << std::endl;
		
		delete[] S;
	}
	
	return 0;
}





















