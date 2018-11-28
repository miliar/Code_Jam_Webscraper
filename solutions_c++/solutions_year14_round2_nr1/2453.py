#include <iostream>
#include <string>
using namespace std;

string B;
int check(string A, int i)
{
	int count1 = 0, count2 = 0;
	int count= 0;
	if(i == 0)
	{
		B = A;
		return 0;
	}
	if(A[0] != B[0])
	{
		return -1;
	}
	
	int  x = 0, y = 0;
	int l1 = A.size();
	int l2 = B.size();
	while(x < l1 || y < l2)
	{
		if(A[x] == B[y])
		{
			x++;
			y++;
		}
		else if(A[x] == A[x-1])
		{
			count1++;
			x++;
			count++;
		}
		else if(B[y] == B[y-1])
		{
			y++;
			count2++;
			count++;
		}
		else
		{
			return -1;
		}
	}
	if(x == l1 && y == l2)
	{
		B = A;
		return count;
		//return count1>count2?count1:count2;
	}
}

int main() {
	// your code goes here
	int T, N;
	int max = 0, ret = 0;
	cin>>T;
	for(int i = 1; i <= T; i++)
	{
		B.clear();
		max = 0;
		ret = 0;
		cin>>N;
		for(int j =0; j< N; j++)
		{
			string A;
			cin>>A;
			ret = check(A, j);
			if(ret == -1)
			{
				max = -1;
				break;
			}
			if(ret > max)
			{
				max=ret;
			}
		}
		if(max == -1)
		{
			cout<<"Case #"<<i<<": "<< "Fegla Won"<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<< max<<endl;
		}
	}
	return 0;
}
