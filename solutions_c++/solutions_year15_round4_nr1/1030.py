#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(){
	cout<<"launching function main"<<endl;
	ifstream file("A-large.in");
	ofstream outputfile("myoutput.txt");
	int T, R, C, tochange;
	char mychar;
	vector<int> arrow, smallestRow, largestRow, smallestColumn, largestColumn;//0: empty; 1:up; 2=right; 3: down; 4: left
	bool possible, localpossible;
	file>>T;
	for(int t=0;t<T;t++){
		//read input
		file>>R>>C;
		arrow.resize(R*C);
		smallestRow.resize(C);largestRow.resize(C);
		smallestColumn.resize(R);largestColumn.resize(R);
		for(int i=0;i<R;i++){
			smallestColumn[i]=C;largestColumn[i]=-1;
		}
		for(int j=0;j<C;j++){
			smallestRow[j]=R;largestRow[j]=-1;
		}
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				file>>mychar;
				switch(mychar){
					case '.': arrow[C*i+j]=0; break;
					case '^': arrow[C*i+j]=1; break;
					case '>': arrow[C*i+j]=2; break;
					case 'v': arrow[C*i+j]=3; break;
					case '<': arrow[C*i+j]=4; break;
					default: cout<<"ERROR : unrecognized character : "<<mychar<<endl;
				}
				if(mychar != '.'){
					smallestRow[j]=min(smallestRow[j], i);
					largestRow[j]=max(largestRow[j], i);
					smallestColumn[i]=min(smallestColumn[i], j);
					largestColumn[i]=max(largestColumn[i], j);
				}
			}
		}
		//solve
		possible=true;
		tochange=0;
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				if(arrow[C*i+j] !=0){
					switch(arrow[C*i+j]){
						case 1:
							if(smallestRow[j]>=i)
								tochange++;
							break;
						case 2:
							if(largestColumn[i]<=j)
								tochange++;
							break;
						case 3:
							if(largestRow[j]<=i)
								tochange++;
							break;
						case 4:
							if(smallestColumn[i]>=j)
								tochange++;
							break;
						default: cout<<"unexpected number !"<<endl;
					}
					localpossible=((smallestRow[j]<i)||(largestColumn[i]>j)||(largestRow[j]>i)||(smallestColumn[i]<j));
					possible=possible&&localpossible;
				}
			}
		}
		//write output
		if(possible)
			outputfile<<"Case #"<<(t+1)<<": "<<tochange<<endl;
		else
			outputfile<<"Case #"<<(t+1)<<": "<<"IMPOSSIBLE"<<endl;
	}
	file.close();
	outputfile.close();
}

