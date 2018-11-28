#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <array>

using namespace std;

#define MAX_SIZE 100

struct lawncell{
	int x;
	int y;
	int height;
	bool possible;
	lawncell(int a,int b,int c,bool d){
		x=b;
		y=a;
		height=c;
		possible=d;
	}
	lawncell(){
	}
};

static bool isPossible(lawncell yes, lawncell may){
	//yes should be possible, may is being tested
	//cells should be adjacent
	return yes.possible&&yes.height <= may.height;
}

int main(){
	istream * stream;
	ifstream myfile;
	myfile.open("B-large.in");

	ofstream outfile;
	outfile.open("output.txt");
	
	if(myfile.is_open()){
		stream = &myfile;
	}else{
		stream = &cin;
	}

	int num;

	(*stream) >> num;

	for(int i=0;i<num;i++){
		//input goes here

		int height, width;
		(*stream)>>height>>width;

		array<array<lawncell *,MAX_SIZE>,MAX_SIZE> lawn;
		int ht;

		for(int h=0;h<height;h++){
			for(int w=0;w<width;w++){
				(*stream) >> ht;
				lawncell * lc = new lawncell(h,w,ht,
					false);
				lawn[h][w]=lc;
			}
		}

		//solving goes here


		int max;

		//go thru rows and cols...
		for(int r=0;r<height;r++){
			max=0;
			for(int c=0;c<width;c++){
				if(lawn[r][c]->height>max){
					max=lawn[r][c]->height;
				}
			}
			for(int c=0;c<width;c++){
				if(lawn[r][c]->height==max){
					lawn[r][c]->possible=true;
				}
			}
		}

		for(int c=0;c<width;c++){
			max=0;
			for(int r=0;r<height;r++){
				if(lawn[r][c]->height>max){
					max=lawn[r][c]->height;
				}
			}
			for(int r=0;r<height;r++){
				if(lawn[r][c]->height==max){
					lawn[r][c]->possible=true;
				}
			}
		}

		//finally, check if everytihngs mowed...
		bool allMowed = true;
		for(int r=0;r<height;r++){
			for(int c=0;c<width;c++){
				if(!lawn[r][c]->possible){
					allMowed=false;
				}
			}
		}
		
			outfile << "Case #" << i+1 << ": ";
		if(allMowed){
			outfile << "YES";
		}else outfile <<"NO";
		outfile << endl;
	}
}