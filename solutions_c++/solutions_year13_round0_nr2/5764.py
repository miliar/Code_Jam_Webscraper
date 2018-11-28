#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <string>

std::ifstream input;
std::ofstream output;
int n,m;
const int nMax = 100;
const int mMax = 100;
const short aij = 2;
int* field;
int k,j,rightIndex,leftIndex;

inline bool IsLeft()
{
	if(k == 0)
		return false;
	for(int h=k; h >= 0; h--)
		if(field[j*m + k] < field[j*m +h])
		{
			leftIndex = h+1;
			return true;
		}
	return false;
}

inline bool IsRight()
{
	if(k == m-1)
		return false;
	for(int h=k; h < m; h++ )
		if(field[j*m + k] < field[j*m + h])
		{
			rightIndex = h - 1;
			return true;
		}
	return false;
}

inline bool IsUp(int g,int p)
{
	if(j == 0)
		return false;

	for(int h=0; h < j; h++ )
		if(field[g*m + p] < field[(h)*m + p])
			return true;
	return false;
}

inline bool IsDown(int g, int p)
{
	if(j == n-1)
		return false;
	for(int h=j; h < n; h++ )
		if(field[j*m + p] < field[(h)*m + p])

			return true;
	return false;
}

int main()
{
	input.open("task.in");
	output.open("taskResult.out");
	field = (int*)::malloc(sizeof(short)*mMax*nMax);
	int countCases;
	input >> countCases;
	for(int i=0; i < countCases; i++)
	{
		input >> n >> m;
		for(j=0; j < n; j++)
		{
			for(k=0; k < m; k++)
			{
				input >> field[j*m + k];
				printf("%d",field[j*m +k]);
			}
			printf("%d\n");
		}
		if(n == 1 || m == 1)
		{
			output << "Case #" << i+1 << ": YES\n";
			printf(": YES\n");
		}
		else
		{
			bool isEnd = false;
			bool isResult = true;
			for(j=0; j < n; j++)
			{
				if(isEnd)
					break;
				for(k=0; k < m; k++)
				{
					rightIndex = m;
					leftIndex = k;
					bool isLeft = IsLeft();
					bool isRight = IsRight();
					if(isLeft || isRight)
					{
						bool localEnd = false;
						if(leftIndex == rightIndex)
						{
							for(int w=0; w < n; w++)
							{
								bool isUp = IsUp(w,leftIndex);
								bool isDown = IsDown(w,leftIndex);
								if(isUp || isDown)
								{
									localEnd = true;
									isResult = false;
									isEnd = true;
									break;
								}
								if(localEnd)
									break;
							}
						}
						for(int q=leftIndex; q < rightIndex; q++)
						{
							for(int w=0; w < n; w++)
							{
								bool isUp = IsUp(w,q);
								bool isDown = IsDown(w,q);
								if(isUp || isDown)
								{
									localEnd = true;
									isResult = false;
									isEnd = true;
									break;
								}
								if(localEnd)
									break;
							}
						}
						if(localEnd)
							break;
					}
				}
			}
			if(isResult)
			{
				output << "Case #" << i+1 << ": YES\n";
				printf(": YES\n");
			}
			else
			{
				output << "Case #" << i+1 << ": NO\n";
				printf(": NO\n");
			}
		}
	}
	input.close();
	output.flush();
	output.close();
   return 0;
}