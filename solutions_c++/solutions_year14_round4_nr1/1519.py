#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <ttmath/ttmath.h>
#include <homemade/graph.cc>
#include <homemade/dijkstra.cc>

#define wrapper(i) std::cout << "Case #" << i << ": "

/*
void print_tab(int tab[][1], int size) {
	for (int i=0; i<size; i++) {
		for (int j=0; j<size; j++)
			std::cout << tab[i][j];
		std::cout << std::endl;
	}
	return;
}
/**/

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int cases;
	std::cin >> cases;
	for (int test_case=1; test_case<=cases; test_case++) {
        int N, X;
        int files[10000];
        std::cin >> N >> X;
        for (int i=0; i<N; ++i)
            std::cin >> files[i];
        std::sort(files, files+N);
        std::reverse(files, files+N);
        int disks = 0;
        int moved[10000];
        for (int i=0; i<N; ++i)
            moved[i] = 0;
        for (int i=0; i<N; ++i) {
            if (moved[i])
                continue;
            for (int j=i+1; j<N; ++j)
                if (!moved[j] && files[i]+files[j] <= X) {
                    ++moved[j];
                    break;
                }
                ++moved[i];
                ++disks;
        }

		wrapper(test_case);
		std::cout << disks << "\n";

	}

	return 0;
}

