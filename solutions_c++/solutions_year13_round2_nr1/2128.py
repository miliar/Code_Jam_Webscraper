#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::sort;
typedef struct Unit{
	int current;
	int operation;
	int loc;
}Unit;
void prob1(){
	int T, A, N;
	cin>>T;
	for(int caseNo=0; caseNo < T; caseNo++){
		cin>>A>>N;
		vector<int> motes;
		int total = 0;
		for(int i=0; i<N; i++){
			int m;
			cin>>m;
			total+= m;
			motes.push_back(m);
		}
		sort(motes.begin(), motes.end());
		vector<Unit> stack;
		int currentSize = A;
		int openrations=0;
		int minOp=N;
		Unit u;
		u.current = A;
		u.loc = 0;
		u.operation = 0;
		stack.push_back(u);
		while(!stack.empty()){
			Unit tmp = stack.back();
			stack.pop_back();
			if(tmp.operation >= minOp)continue;
			while(tmp.loc < motes.size() && tmp.current>motes[tmp.loc]){
				tmp.current+=motes[tmp.loc];
				tmp.loc++;
			}
			if(tmp.loc >= motes.size()){
				if(tmp.operation < minOp){
					minOp = tmp.operation;
				}
				continue;
			}
			if(tmp.current <= motes[tmp.loc]){
				Unit newU1;
				newU1.current = tmp.current*2-1;
				newU1.operation = tmp.operation+1;
				newU1.loc = tmp.loc;
				stack.push_back(newU1);
				Unit newU2;
				newU2.current = tmp.current;
				newU2.operation = tmp.operation+1;
				newU2.loc = tmp.loc+1;
				stack.push_back(newU2);
			}
		}
		cout<<"Case #"<<caseNo+1<<": "<<minOp<<endl;
	}
}
void prob2(){

}
int main(){
	prob1();
	return 0;
}
