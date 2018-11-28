#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <iomanip>

struct Data{
	int n;
	int m;
	std::vector<int> data;
};

std::string trial(const Data& input){
	std::vector<std::vector<int> > a(input.n, std::vector<int>(input.m,0));

	for(int i=0; i<input.data.size(); i++){
		a[i/input.m][i%input.m] = input.data[i];
	}

	for(int i=0;i<input.n; i++){
		for(int j=0;j<input.m;j++){
			// 行方向
			bool flag1=true;
			for(int y=0;y<input.n;y++){
				if(a[i][j] < a[y][j]){
					flag1=false;
					break;
				}
			}

			// 列方向
			bool flag2=true;
			for(int x=0;x<input.m;x++){
				if(a[i][j] < a[i][x]){
					flag2=false;
					break;
				}
			}

			if(flag1==false && flag2==false) return "NO";
		}
	}

	return "YES";
}

int main(int argc, char **argv){
	std::string str;
	int t;

	std::cin >> t;
	std::vector<Data> query(t);
	for(int i=0;i<t;i++){
		int c;
		std::cin >> query[i].n;
		std::cin >> query[i].m;
		int size=query[i].n*query[i].m;
		for(int j=0;j<size;j++){
			std::cin >> c;
			query[i].data.push_back(c);
		}
	}

	std::vector<std::string> result(t);
#ifdef _OPENMP
#pragma omp parallel for
#endif
	for(int i=0;i<t;i++){
		result[i]=trial(query[i]);
	}

	for(int i=0;i<t;i++){
		std::cout << "Case #" << i+1 << ": " << result[i] << std::endl;
	}
	return 0;
}
