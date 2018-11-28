#include <iostream>
#include <algorithm>

bool magia(int size, int rows, int cols){
	if(rows*cols%size not_eq 0) return true;
	if(rows < size) return true;
	if(size==3){
		return rows==3 and cols==1;
	}
	if(size==4){
		return 
			rows==4 and cols==1 
			or rows==4 and cols==2;
	}
	return false;
}

int main(int argc, char **argv){
	int casos;
	std::cin>>casos;
	for(int K=1; K<=casos; ++K){
		int size, rows, cols;
		std::cin >> size >> rows >> cols;
		if(rows<cols) std::swap(rows, cols);
		bool win = magia(size, rows, cols);
		std::cout << "Case #" << K << ": " << (win?"RICHARD":"GABRIEL") << '\n';
	}
	return 0;
}
