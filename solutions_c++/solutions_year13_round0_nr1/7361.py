#include <iostream>
#include <string>
#include <vector>
using std::vector;
using std::string;


int main(void){
	using namespace std;
	const int K=4;
	const string kXWon="X won";
	const string kOWon="O won";
	const string kDraw="Draw";
	const string kGoon="Game has not completed";

	int T;cin>>T;
	for(int X=1;X<=T;X++){
		string square[K];
		for(long index=0;index<K;index++){
			cin>>square[index];
		}
		cin.ignore();
		string result="";
		int s = 0;
		//
		// to do
		bool oTate[K],oYoko[K];
		bool xTate[K],xYoko[K];
		bool oMigiNaname=true;bool oHidariNaname=true;
		bool xMigiNaname=true;bool xHidariNaname=true;
		int cntDot=0;
		for(int i=0;i<K;i++){
			oTate[i]=true;
			oYoko[i]=true;
			xTate[i]=true;
			xYoko[i]=true;
		}
		for(int row=0;row<K;row++){
			for(int col=0;col<K;col++){
				switch(square[row][col]){
					case 'X':
						oTate[col]=false;
						oYoko[row]=false;
						if(row==col){
							oMigiNaname=false;
						}else if(row==K-col-1){
							oHidariNaname=false;
						}
						break;
					case 'O':
						xTate[col]=false;
						xYoko[row]=false;
						if(row==col){
							xMigiNaname=false;
						}else if(row==K-col-1){
							xHidariNaname=false;
						}
						break;
					case 'T':
						break;
					case '.':
						cntDot++;
						oTate[col]=false;
						oYoko[row]=false;
						xTate[col]=false;
						xYoko[row]=false;
						if(row==col){
							oMigiNaname=false;
							xMigiNaname=false;
						}else if(row==K-col-1){
							oHidariNaname=false;
							xHidariNaname=false;
						}
						break;
				}
			}
		}
		bool o=oMigiNaname|oHidariNaname;
		bool x=xMigiNaname|xHidariNaname;
		for(int i=0;i<K;i++){
			o|=oTate[i]|oYoko[i];
			x|=xTate[i]|xYoko[i];
		}
		if(x){
			s=0;
		}else if(o){
			s=1;
		}else if(cntDot==0){
			s=2;
		}else{
			s=3;
		}
		//
		switch(s){
			case 0:
				result=kXWon;
				break;
			case 1:
				result=kOWon;
				break;
			case 2:
				result=kDraw;
				break;
			case 3:
				result=kGoon;
				break;
			default:
				break;
		}
		cout<<"Case #"<<X<<": "<<result<<endl;
	}
	cout.flush();
	cerr.flush();
	return 0;
}
