#include <iostream>
#include <vector>

using namespace std;

vector<int> numbersSize;
int x,y,k,A,N,AN;

bool removePossibilies(void){
	int z=1;
	//cout << "Removing smaller numbers" << endl;
	while (z!=0) {
		z=0;
		for (k=0;k<numbersSize.size();k++){	
			if (A>numbersSize[k]){
				A+=numbersSize[k];
				numbersSize.erase(numbersSize.begin() + k);
				k--;
				z++;
			}
		}
	}
	if (numbersSize.size()==0) return true;
	else return false;
}

int takeSmaller(void){
	//cout << "Getting smaller number" << endl;	
	int small=1000000;
	for (k=0;k<numbersSize.size();k++) if (numbersSize[k]<small) small=numbersSize[k];
	return small;
}

int stepsToNumber(int i, int d){
	//cout << "Calculating Steps" << endl;	
	int c;
	if (i!=1){
		while (i<d){
			i=(2*i)-1;
			c++;
		}
		return c;
	}
	return 1000000;
}

int takeNumBigger(void){
	//cout << "Getting Number of Biggers" << endl;
	int bigN=0;
	for (k=0;k<numbersSize.size();k++) if (numbersSize[k]>=A*2) bigN++;
	return bigN;
}

bool removeBiggerNum(void){
	//cout << "Removing bigger number" << endl;	
	int big=0;
	int bigIndex;
	for (k=0;k<numbersSize.size();k++) if (numbersSize[k]>big){
		big=numbersSize[k];
		bigIndex=k;
	}
	numbersSize.erase(numbersSize.begin() + bigIndex);
	N--;
	return true;
}

int main (void)
{
	int num;
	cin >> num;
	
	for (x=0;x<num;x++){
		cin >> A;			//Armin Size
		cin >> N;			//Motes Number
			//Motes Sizes
		for (k=0;k<N;k++){
			cin >> AN;
			numbersSize.push_back(AN);
		}
		
		y=0;
		while(!removePossibilies()){
			if (takeSmaller()<(A+A-1)){
				//cout << "Growing" << endl;
				A+=A-1;
				y++;
			}
			else {
				if (stepsToNumber(A,takeSmaller())>takeNumBigger()){
					//cout << "Removing bigger number" << endl;
					removeBiggerNum();
					y++;
				}
				else {
					//cout << "Last option" << endl;
					A+=A-1;
					y++;
				}

			}

		}
		cout << "Case #" << x+1 << ": " << y << endl;
		
		numbersSize.clear();
	}
	
	return 0;
}
