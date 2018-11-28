#include <ostream>
#include <iostream>

struct Point{
	int row, col;
	Point(int prow, int pcol) : row(prow), col(pcol) {}
};

class Lawn{
	const int row, col;
	int *mGrid;
public:
	Lawn(int prow, int pcol) : row(prow), col(pcol){
		mGrid = new int[row*col];
		for(int i = 0; i < row; i++){
			for(int j = 0; j < col; j++){
				std::cin >> mGrid[i*col + j];
			}
		}
	}

	~Lawn(){delete [] mGrid;}

	int at(const Point& p) const{
		return mGrid[p.row*col + p.col];
	}

	int at(int prow, int pcol) const{
		return mGrid[prow*col + pcol];
	}

	bool checkRow(int prow, int value) const{
		for(int i = 0; i < col; i++){
			if(this->at(prow,i) > value){
				return false;
			}
		}
		return true;
	}

	bool checkCol(int pcol, int value) const{
		for(int i = 0; i < row; i++){
			if(this->at(i,pcol) > value){
				return false;
			}
		}
		return true;
	}

	bool solve(void) const{
		for(int i = 0; i < row; i++){
			for(int j = 0; j < col; j++){
				const int v = this->at(i,j);
				if(!(this->checkRow(i,v) || this->checkCol(j,v))){
						return false;
				}
			}
		}
		return true;
	}

//	friend std::ostream& operator <<(std::ostream& pStream, const Lawn& l);
};
/*
std::ostream& operator <<(std::ostream& pStream, const Lawn& l){
	for(int i = 0; i < l.row; i++){
		for(int j = 0; j < l.col; j++){
			pStream << l.at(Point(i,j)) << " ";
		}
		pStream << std::endl;
	}
	return pStream;
}*/

int main(void){
	int NumCases;
	std::cin >> NumCases;
	int testCase = 0;
	while(testCase < NumCases){
		int row, col;
		std::cin >> row >> col;
		Lawn l(row,col);
//		std::cout << l;
		if(l.solve()){
			std::cout << "Case #" << ++testCase << ": YES" << std::endl;
		}
		else{
			std::cout << "Case #" << ++testCase << ": NO" << std::endl;
		}
	}
	return 0;
}