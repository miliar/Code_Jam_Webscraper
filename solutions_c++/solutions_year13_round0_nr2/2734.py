#include <iostream>
using namespace std;

#define MAX_HEIGHT 2
#define print { \
    for (int i=0; i < N; i++)\
    {\
	for (int j=0; j < M; j++)\
	{\
	    cout << Lawn[i][j] << " ";\
	}\
	cout << endl;\
    }\
    }

int main()
{
    int T, N, M;
    string result;

    cin >> T;

    for(int n = 0; n < T; n++)
    {
	cin >> N >> M;

	int Result[N][M];
	
	for (int i = 0; i < N; i++)
	{
	    for (int j = 0; j < M; j++)
	    {
		cin >> Result[i][j]; 
	    }
	}
    
	int Lawn[N][M];	

	for (int i = 0; i < N; i++)
	{
	    for (int j = 0; j < M; j++)
	    {
		Lawn[i][j] = MAX_HEIGHT;
	    }
	}

	//print;
	
	int height = MAX_HEIGHT - 1;	

	for (int i = 0; i < N; i++)
	{
	    int mow = 0;
	
	    for (int j = 0; j < M; j++)
	    {   
		if (Result[i][j] == height)
		{
		    mow++;
		}
	    }
	    if (mow == M)
	    {
		for (int j = 0; j < M; j++)
		{   
		    Lawn[i][j] = height;
	        }
	    }
	}
	
	//print;

	for (int j = 0; j < M; j++)
	{
	    int mow = 0;

	    for (int i = 0; i < N; i++)
	    {   
		if (Result[i][j] == height)
		{
		    mow++;
		}
	    }
	    if (mow == N)
	    {
		for (int i = 0; i < N; i++)
		{
		    Lawn[i][j] = height;
		}
	    }
	
	}

	//print;

	result = "YES";

	for (int i = 0; i < N; i++)
	{   
	    for (int j = 0; j < M; j++)
	    {
		if (Lawn[i][j] != Result[i][j])
		{
		    result = "NO";
		}
	    }
	}	

	cout << "Case #" << n+1 << ": " << result << endl;
    }

    return 0;
}
