#include<iostream>
#include<fstream>
#include<math.h>
#include<vector>
#include<algorithm>

using namespace std;


int main()
{
	ifstream inpFile;
	inpFile.open("input.txt");
	ofstream outFile;
	outFile.open("output.txt");
	unsigned int T;
	inpFile>>T;
	unsigned int A, N, temp;

	for(unsigned int i=0; i<T; i++)
	{
		inpFile>>A>>N;
		vector<int>M;
		for(int n=0; n<N; ++n)
		{
			inpFile>>temp;
			M.push_back(temp);
		}
		sort(M.begin(), M.end());
		int sum = 0;
		for(int n=0; n<N; n++)
		{
			if(A>100)
				break;
			if(A>M[n])
				A += M[n];
			else
			{
				temp = M[n]-A+1;
				if(temp<A && A>1)
				{
					sum++;
					temp = A-1;
					if(temp>100)
						temp = 100;
					A += temp;
					n--;
				}
				else
				{
					temp = N-n;
					if(temp<=2 || A==1)
					{
						sum+=temp;
						break;
					}
					int j;
					for(j=2; j<temp; j++)
					{
						int tempA = A;
						int k;
						for(k=0; k<j; ++k)
						{
							tempA += (tempA-1);
						}
						for(k=0; k<j+1; ++k)
						{
							if(tempA>M[n+k])
							{
								tempA+=M[n+k];
							}
							else
								break;
						}
						if(k==(j+1))
						{
							sum += j;
							A = tempA;
							break;
						}
					}
					if(j==temp)
					{
						sum += N-n;
						break;
					}
				}
			}
		}

		outFile<<"Case #"<<i+1<<": "<<sum<<endl;
	}
	

	

}