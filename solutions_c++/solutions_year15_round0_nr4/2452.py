#include "iostream"
#include "fstream"
#include "vector"
#include "math.h"
#include "string"

using namespace std;


int main(){
    int T;
    ifstream in("input2.txt");
    ofstream out("output.txt");
    in >>T;
    for(int i=0;i<T;i++){
		int X, R, C;
		in>>X>>R>>C;
		out<<"Case #"<< i+1<<": ";
		if(X>=7){
			out<<"RICHARD"<<endl;
			continue;
		}
		if(X==4||X==6){
			if(max(R,C)<X||min(R,C)<(X+1)/2+1||R*C%X!=0){
				out<<"RICHARD"<<endl;
				continue;
			}
			else{
				out<<"GABRIEL"<<endl;
				continue;
			}
		}
		else{
			if(max(R,C)<X||min(R,C)<(X+1)/2||R*C%X!=0){
				out<<"RICHARD"<<endl;
				continue;
			}
			else{
				out<<"GABRIEL"<<endl;
				continue;
			}
		}
	}
}
