#include <string>
#include <cmath>
#include <vector>
#include <cstdio>
#include <fstream>

long long p_num[40] = {
	1, 4, 9, 121, 484, 
	10201, 12321, 14641, 40804, 44944, 
	1002001, 1234321, 4008004, 100020001, 102030201, 
	104060401, 121242121, 123454321, 125686521, 400080004, 
	404090404, 10000200001, 10221412201, 12102420121, 12345654321, 
	40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 
	1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 
	1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001 }; 

bool is_p_num(long long x)
{
	char num_string[20] = "";
	sprintf(num_string, "%lld", x);
	for (int i=0; i < strlen(num_string); i++) {
		int strlength = strlen(num_string);
		if (num_string[i] != num_string[strlength-i-1]) {

			return false;
		}
	}

	return true;
}
void search_for_scope(long long int x, int& left, int& right)
{
	
	while (left <= right)
	{
		int mid = (left+right)/2;
		if (x < p_num[mid])
		{
			right = mid-1;
		}
		else if (x == p_num[mid])
		{
			left = mid;
			right = mid;
			return;
		}
		else 
		{
			left = mid+1;
		}
	}
}

int main()
{
	std::ofstream out;
	std::ifstream in;
	in.open("a.in");
	out.open("a.out");
	int Case;

	in >> Case;
	for (int t=1; t<=Case; t++)
	{
		long long A, B;
		// cin >> A >> B;
		in >> A >> B;
		int cnt = 0;
		int left, right, start, end;
		left = 0, right = 39;
		search_for_scope(A, left, right);
		start = left;
		left = 0, right = 39;
		search_for_scope(B, left, right);
		end = right;
		cnt = end - start + 1;
		out << "Case #" << t << ": " << cnt << std::endl;
	}
	out.close();

	return 0;
}