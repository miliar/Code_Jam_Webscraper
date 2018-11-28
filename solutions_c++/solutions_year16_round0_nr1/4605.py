#include "set"
#include "cstdio"

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d", &t);
	for (int testcase = 0; testcase < t; ++testcase) {
		int x;
		scanf("%d", &x);
		int i = 1;
		set<int> st;
		for (int i = 0; i < 10; ++i)
		{
			st.insert(i);
		}
		while (!st.empty() && i < 1000000) {
			int tmp = x*i;
			while (tmp > 0) {
				st.erase(tmp%10);
				tmp /= 10;
			}
			i++;
		}
		printf("Case #%d: ", testcase+1);
		if (st.empty())
		{
			printf("%d\n", x*(i-1));
		} else {
			printf("INSOMNIA\n");
		}
		
	}
	return 0;
}