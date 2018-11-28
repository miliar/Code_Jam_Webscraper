#include <iostream>
#include <string>
#include <algorithm>
#include <functional>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>

bool display(unsigned int **a, unsigned int N, unsigned int M) {
	for(unsigned int n=0; n<N; ++n) {
		for(unsigned int m=0; m<M; ++m)
			std::cout << a[n][m] << " ";
		std::cout << std::endl;
	}
	std::cout << std::endl;
	
	return false;
}

static bool** visited;

bool solve(unsigned int **a, unsigned int N, unsigned int M) {
	bool result = true;
	// 通過フラグ
	visited = new bool*[N];
	for(unsigned int n=0; n<N; ++n) {
		visited[n] = new bool[M];
		for(unsigned int m=0; m<M; ++m) visited[n][m] = false;
	}
	
	for(unsigned int n=0; n<N; ++n) {
		for(unsigned int m=0; m<M; ++m) {
			visited[n][m] = true;
			if(a[n][m] == 1) {
				for(unsigned int _n=0; _n<N; ++_n) {if(a[_n][m] != 1) {
					for(unsigned int _m=0; _m<M; ++_m) {if(a[n][_m] != 1) {
						result = false; goto END_LOOP;
					}}
				}}
			}
		}
	}
	
END_LOOP:
	for(unsigned int n=0; n<N; ++n) delete visited[n];
	delete visited;
	
	return result;
}

int main(int argc, char** argv) {
	unsigned int T;
	std::cin >> T;
	
	for(unsigned int t=0; t<T; ++t) {
		unsigned int N, M;
		std::cin >> N >> M;
		
		unsigned int **a = new unsigned int*[N];
		for(unsigned int n=0; n<N; ++n) {
			a[n] = new unsigned int[M];
			for(unsigned int m=0; m<M; ++m)
				std::cin >> a[n][m];
		}
		
		//display(a, N, M);
		
		std::cout << "Case #" << (t+1) << ": " << (solve(a, N, M) ? "YES" : "NO") << std::endl;
		
		for(unsigned int n=0; n<N; ++n) delete a[n];
		delete a;
	}
	
	return 0;
}
