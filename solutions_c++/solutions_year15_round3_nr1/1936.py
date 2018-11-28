#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<bitset>
#include<map>
#include<set>

using namespace std;


int mem[100][100][2] = {0};

int func2(int lent, int d, bool b)
{
	if(lent  == 0)
		return 0;

	if(mem[lent][d][b] == 0)
	{
		int res = 100000;


		if(lent < d && !b)
			res = 0;
		else if(lent == d && !b)
			res = 1;
		else if(lent < d && b)
		{
			res = -100000000;
		}
		else if(lent == d && b)
		{
			return lent;
		}
		else
		{

			for(int i = 1; i <= lent; i++)
			{
				int res1, res2;
				if(b)
				{
					res1 = func2(lent - i, d, true) + func2(i - 1, d, false) + 1;
					res2 = func2(lent - i, d, false) + func2(i - 1, d, true) + 1;
				}
				else
				{
					res1 = func2(lent - i, d, false) + func2(i - 1, d, false) + 1;
					res2 = func2(lent - i, d, false) + func2(i - 1, d, false) + 1;
				}

				int res_ = max(res1, res2);

				int res0 = (i == 1 || i == lent) ? d : d + 1; 



				res = min(res, max (res0, res_));
			}
			
			
		}
		mem[lent][d][b] = res;
		
	}
	return mem[lent][d][b];
}

//int func(int lent, int d)
//{
//	if(lent  == 0)
//		return 0;
//
//	if(mem[lent][d] == 0)
//	{
//		int res = 10000;
//		if(lent <= d)
//			res = 1;
//		else
//		{
//			{
//				for(int i = 1; i < lent; i++)
//				{
//					res = min(res, func(lent - i, d) + func(i - 1, d)); 
//				}
//				res++;
//			}
//			
//			
//		}
//		mem[lent][d] = res;
//		
//	}
//	return mem[lent][d];
//}
//
//
//int GetRes(int lent, int d, bool b = true)
//{
//	int res = 0;
//	if(b)
//	{
//		for(int i = 1; i <= lent; i++)
//		{
//			int res1 = min(res, GetRes(lent - i, d, true) + GetRes(i - 1, d, false)) + 1; 
//			int res2 = min(res, GetRes(lent - i, d, false) + GetRes(i - 1, d, true)) + 1; 
//			int res3 = (i == 1 || i == lent) ? d : d + 1; 
//			res = min(res, max (res1, res2));
//		}
//		res += d;
//	}
//	else
//	{
//		res = func(lent, d);
//	}
//	return res;
//}
//
//
//int GetRes2(int lent, int d)
//{
//	int res = 0;
//	for(int i = d; i <= lent; i++)
//	{
//		res = max(res, func(lent - i, d) + func(i - d, d)); 
//	}
//	res += d;
//	return res;
//}


int main()
{
	
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int t;
	cin >> t;
	for(int tt = 0; tt < t; tt++)
	{

		int r, c, w;
		cin >> r >> c >> w;
		int res = func2(c, w, true) * r;

		//if(w == 1)
		//{
		//	res = r * c;
		//}
		//else
		//{
		//	for(int i = 0; i < c; )
		//	{
		//		res++;
		//		i += w - 1;
 	//		}
		//}



		printf("Case #%d: %d\n", tt+1, res);
	}


	return 0;

}