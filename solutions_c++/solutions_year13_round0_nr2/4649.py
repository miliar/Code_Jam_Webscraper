#include <cstdio>
#include<iostream>  
#include<fstream>

#define TAG_X 0x10
#define TAG_O 0x20
#define TAG_XO (TAG_X | TAG_O)
#define TAG_P (0x80 | TAG_XO)
#define TAG_T 0x01

bool parse(char buf[128][128], int N, int M)
{
	char argH[128] = {0};
	char argV[128] = {0};
	for(int i=0; i<N; ++i)
	{
		for(int j=0; j<M; ++j)
		{
			if(argH[i] < buf[i][j])
			{
				argH[i] = buf[i][j];
			}
			if(argV[j] < buf[i][j])
			{
				argV[j] = buf[i][j];
			}
		}		
	}
	for(int i=0; i<N; ++i)
	{
		for(int j=0; j<M; ++j)
		{
			if(buf[i][j] < argH[i] && buf[i][j] < argV[j])
			{
				return false;
			}
		}
	}	
	return true;
}

int main(int argc, char *argv[])
{
	std::ofstream os;
	os.open("B-large.out");

	std::ifstream is;
	is.open("B-large.in");
	if(!is)
	{
		std::cout << "Open file failed" << std::endl;
		return 1;
	}
	int T;
	is >> T;
	char data[128][128];
	for(int i=0; i<T; ++i)
	{
		int N;
		int M;
		is >> N >> M;
		for(int j=0; j<N; ++j)
		{
			for(int k=0; k<M; ++k)
			{
				int V;
				is >> V;
				data[j][k] = (char)V;
			}
		}
		os << "Case #" << i+1 << ": ";
		bool ret = parse(data, N, M);
		os << (ret ? "YES" : "NO") << std::endl;
	}
}
