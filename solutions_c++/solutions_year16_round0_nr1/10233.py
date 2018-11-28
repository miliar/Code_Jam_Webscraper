#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int T, n;
bool b[10];

int main()
{
	scanf("%d",&T);
	for(int z=0; z < T; z++)
	{
		scanf("%d", &n);
		fill(b, b + 10, 0);
		int cnt = 0;

		if (n == 0) {
			printf("Case #%d: INSOMNIA\n",z+1);
			continue;
		}

		int s = n;
		while(1) {
			stringstream ss;
			ss<<s;
			string num;
			ss>>num;
			for (int i = 0; i < num.size(); i++){
				int d = num[i] - '0';
				if (! b[d]) {
					b[d] = 1;
					cnt ++;
				}
			}

			if (cnt == 10)
				break;
			s += n;
		}

		printf("Case #%d: %d\n",z+1,s);
	}

	return 0;
}