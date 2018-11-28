#include<iostream>
#include<fstream>
#include<vector>

typedef unsigned int uint;
typedef unsigned long long ull;
typedef ull resType;

struct pair {
	ull s,e,c;
};

struct prob {
	ull N;
	std::vector<pair> P;
};

long long mcost(long long L)
{
	return L*(L-1)/2;
}

resType doit(const prob P)
{
	resType R = 0;
	
	ull NORMAL = 0;
	for (ull i=0; i<P.P.size(); i++)
		NORMAL += mcost(P.P[i].e-P.P[i].s)*P.P[i].c;
	
// 	std::cout << NORMAL << "\n";
	
	std::vector<int> DEG(P.N+1);
	for (ull i=0; i<P.P.size(); i++)
		for (ull j=P.P[i].s; j<P.P[i].e; j++)
			DEG[j]+=P.P[i].c;
	
	ull start = 1;
	ull end;
	while (1)
	{
		end = start;
		while (DEG[end])
			end++;
		R += mcost(end-start);
		for (ull i=start; i<end; i++)
			DEG[i]--;
		while (start<P.N && DEG[start]==0)
			start++;
		if (start==P.N)
			break;
	}
	
	
	return R-NORMAL;
}


std::vector<resType> read(std::string fName)
{
	std::vector<resType> R;
	
	std::ifstream ifs(fName);
	int T;
	ifs >> T;
	for (int i=0; i<T; i++)
	{
		prob P;
		int M;
		ifs >> P.N >> M;
		P.P = std::vector<pair>(M);
		for (int l=0; l<M; l++)
			ifs >> P.P[l].s >> P.P[l].e >> P.P[l].c;
		
		R.push_back(doit(P));
	}
	return R;
}

void write(const std::vector<resType>& R)
{
	for (uint i=0; i<R.size(); i++)
		std::cout << "Case #" << i+1 << ": " << R[i] << "\n";
}



int main(int argc, char* argv[])
{

	std::vector<resType> R = read("A-small-attempt0.in");
// 	std::vector<resType> R = read("input");
	write(R);
}
