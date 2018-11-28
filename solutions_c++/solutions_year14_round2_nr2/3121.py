#include <fstream>
#include <algorithm>

using namespace std;
int c =0;
bool binary(long long O, long long N, long long K)
{
	
	long long andd =  O & N;
	
	if (andd < K){
		c++;
		return true;
	}
	else return false;
}
ifstream fin("input.txt");
ofstream fout("output.txt");

int main()
{
	int N, T;
	fin>>T;
	N = 0;
	while(N < T)
	{
	int A, B, K;\
	for(long long i = 0; i < T; i++)
	{
		fin>>A>>B>>K;
				for(long long j = 0; j < B; j++)
		{
			for(int x = 0; x < A; x++)
			{
				if(binary(x,j,K))
				{
					
				}
			}
		}
		
		fout<<"Case #"<<N+1<<": "<<c<<endl;
		N++;
		c =0;
	}
}
}
