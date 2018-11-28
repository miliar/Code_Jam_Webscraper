#include<iostream>
#include<vector>
using namespace std;

typedef struct
{
	int n;
	int index[2];

}Out;

bool can1(vector<int> &p, int &total, int index)
{
	int size = p.size();
	double testSize = total - 1;
	if (testSize == 0) return true;
	double pro = 0;

	for (int i = 0; i < size; i++)
	{
		if (i == index)
		{
			if (p[i] - 1 == 0) continue;
			pro = (p[i] - 1) / testSize;
		}
		else
		{
			if (p[i] - 1 == 0) continue;
			pro = p[i] / testSize;
		}
		if (pro > 0.5) return false;
	}

	return true;

}


bool can2(vector<int> &p, int &total,int index1,int index2)
{
	if (index1 == index2 && p[index1] - 2 < 0) return false;
	int size = p.size();
	double testSize = total - 2;
	if (testSize == 0) return true;
	double pro = 0;

	for (int i = 0; i < size;i++)
	{
		if (i == index1 && i == index2)
		{
		   pro = (p[i] - 2) / testSize;
		}
		else if (i == index1)
		{
		
			pro = (p[i]-1) / testSize;
		}
		else if (i ==index2)
		{
		
			pro = (p[i] - 1) / testSize;
		}
		else
		{
			pro = p[i] / testSize;
		}
		if (pro > 0.5) return false;
	}

	return true;

}


Out test(vector<int> &p,int &total)
{
	int size = p.size();
	double testSize = total - 2;
	Out temp;
	temp.n = 0;

	//2개 검사
	for (int i = 0; i < size; i++)
	{
		if (p[i] >= 1 && total >= 2) //1개 가능
		{
			for (int j = i; j < size; j++) //자신부터 끝까지 검사
			{
				if (can2(p, total, i, j))
				{
					temp.n = 2;
					temp.index[0] = i;
					temp.index[1] = j;
					p[i]--;
					p[j]--;
					total -= 2;
					return temp;
				}
			}
		}

	}

	for (int i = 0; i < size; i++)
	{
		if (p[i] >= 1 && total >= 1) //1개 가능
		{
			for (int j = i; j < size; j++) //자신부터 끝까지 검사
			{
				if (can1(p, total, i))
				{
					temp.n = 1;
					temp.index[0] = i;
					p[i]=p[i]-1;
					total=total-1;
					return temp;
				}
			}
		}
	}
	return temp;
}

int main()
{

	int T;
	cin >> T;
	for (int TestN = 1; TestN <= T; TestN++)
	{

		int total = 0;
		int party;
		cin >> party;
		vector<int> person(party);
		for (int i = 0; i < party; i++)
		{
			cin >> person[i];
			total += person[i];
		}
		cout << "Case #" << TestN << ": ";

		while (total != 0)
		{
			Out cur = test(person,total);		
			for (int i = 0; i < cur.n; i++) cout << (char)(cur.index[i] + 'A');
	
			cout << " ";

		}
		cout << endl;


	}


	return 0;
}