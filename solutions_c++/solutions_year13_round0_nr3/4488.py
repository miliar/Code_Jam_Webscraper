

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <string>
#include <complex>
#include <functional>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <fstream>
using namespace std;

int main() {



	freopen("D:/GCJ2013/C-small-attempt0.in","r", stdin);
	freopen("D:/GCJ2013/C-small-attempt0.out", "w", stdout);
	//freopen("D:/GCJ2013/A-large.in","r", stdin);
	//freopen("D:/GCJ2013/A-large.out", "w", stdout);
	
	bool stage[1024];
	int t;
	memset(stage, false, sizeof(stage));
	stage[0] = stage[1] = stage[4] = stage[9] = stage[121] = stage[484] = true;
	while(scanf("%d", &t) != EOF && t != 0){
		for(int num = 1; num <= t; num++){
			int begin, end;
			scanf("%d%d", &begin, &end);
			int res = 0;
			for(int i = begin; i <= end; i++)
				if(stage[i])res++;
			printf("Case #%d: %d\n", num, res);
		}
	}

    return 0;
}






