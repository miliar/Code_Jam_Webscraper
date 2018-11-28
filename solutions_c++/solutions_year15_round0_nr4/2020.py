#include <vector>
#include <queue>
#include <iostream>
using namespace std;

class BackgroundGrid{
	long long rows;
	long long columns;
	public:
	vector< vector <bool> > isCovered;
	BackgroundGrid(short rows,short columns){
		this->rows = rows;
		this->columns = columns;
	}
};

class NominoSolver{
	int nominoNumber;
	int rows;
	int columns;
	public:
	void input(){
		cin>>nominoNumber>>rows>>columns;
	}
	bool isGabrielWinner(){
		if (nominoNumber == 3){
			if ( ( (rows == 2) && (columns == 3)) 	||   ( (rows == 3) && (columns == 2)) 
	||   ( (rows == 3) && (columns == 3)) 
			||   ( (rows == 3) && (columns == 4)) ||   ( (rows == 4) && (columns == 3))){
				return true;
			}
			else{
				return false;
			}
			
		}else if(nominoNumber == 1){
			return true;
		}else if (nominoNumber == 2){
			if((rows*columns)%2==0){
				return true;
			}else{
				return false;
			}
		}else{
			if ( ( (rows == 3) && (columns == 4)) 
	||   ( (rows == 4) && (columns == 3)) ||   ( (rows == 4) && (columns == 4))){
				return true;
			}
			else{
				return false;
			}
		}
	}
};
int main1() {
	while(true)
	{
		int n;
		cin>>n;
		if(n == 0)
			break;
		queue<int> q;
		for(int i=1;i<=n;i++)
		{
			q.push(i);
		}
		bool timeToThrow = true;
		while(q.size() > 1)
		{
			int i = q.front();
			q.pop();
			if(timeToThrow == true)
			{
				timeToThrow = false;
			}
			else
			{
				q.push(i);
				timeToThrow = true;
			}
		}
		cout<<q.front()<<endl;
	}
	return 0;
}
int main() {
	int nT = 0;
	cin>>nT;
	for(int tC=1;tC<=nT;tC++){
		NominoSolver nominoSolver;
		nominoSolver.input();
		cout<<"Case #"<<tC<<": ";
		if(nominoSolver.isGabrielWinner())
			cout<<"GABRIEL"<<endl;
		else
			cout<<"RICHARD"<<endl;
	}
	return 0;
}
