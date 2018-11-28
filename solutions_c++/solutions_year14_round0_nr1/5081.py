#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

class solution{
public:
	solution(int n){
		num = n;
		cin >>row;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++){
				cin >> cards[i][j];
			}
		for(int i=0;i<4;i++){
			possible[i] = cards[row-1][i];
		}
		
		cin >>row;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++){
				cin >> cards[i][j];
			}
		
		for(int k=0;k<4;k++)
			for(int i=0;i<4;i++){
				if(possible[k]==cards[row-1][i])
					sol.push_back(possible[k]);
			}
		
	}
	~solution(){
		cout<<"Case #"<<num<<": ";
		print();
	}
	void print(){
		if(sol.size()==1){
			cout<<sol[0]<<endl;
		}
		else if(sol.size()>1){
			cout<<"Bad magician!\n";
		}
		else if(sol.size()==0){
			cout<<"Volunteer cheated!\n";
		}
		
	}
private:
	
	int cards[4][4];
	int row,num;
	int possible[4];
	vector<int> sol;
};

int main(){
	int time;
	cin >>time;
	vector<solution*> s;
	for(int i=0;i<time;i++){
		s.push_back(new solution(i+1));
	}
	for(int i=0;i<time;i++){
		delete s[i];
	}
}
