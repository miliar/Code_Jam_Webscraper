#include <iostream>
#include <string>
using namespace std;

//'i' = 105
//'j' = 106
//'k' = 107


// 1    0 
// i    1
// j    2
// k    3
// -1   4
// -i   5
// -j   6
// -k   7
int map[64]={
0,1,2,3,4,5,6,7,
1,4,3,6,5,0,7,2,
2,7,4,1,6,3,0,5,
3,2,5,4,7,6,1,0,
4,5,6,7,0,1,2,3,
5,0,7,2,1,4,3,6,
6,3,0,5,2,7,4,1,
7,6,1,0,3,2,5,4
};

inline int cal(int a,int b){
	return map[a*8+b];
}


inline int getCharCodeAt(string& s, long long iter){
	return s.at(iter % s.size())-104;//i->1, j->2, k->3,   no 1, -?.
}

inline int getInvEle( int a){
	return (a+4)%8;
}

string execute(long long L,long long X, string s){
	long long sMax = L*X;
	int leftCode = 0; // as '1'
	int rightCode = 0;
	if(sMax<=2)return "NO";// at least 3

	leftCode = 0     ;// position: -1
	rightCode= 0     ;//position: 0~end
	for(long long iter = 0 ; iter < sMax ; iter++){
		rightCode = cal(rightCode, getCharCodeAt(s,iter));
	}

	// simple test for finding k's position
	int testCode = 0;
	long long biggestKposition=1;

	for(long long iter = sMax-1 ; iter>=0 ; --iter){
		testCode = cal( getCharCodeAt(s,iter) , testCode      );
		if(testCode==3){
			biggestKposition=iter;
			break;
		}
	}

	for(long long iter = 0 ; iter < sMax-1 && iter<biggestKposition ; ++iter){// first splitter
		leftCode = cal (leftCode,getCharCodeAt(s,iter));   //get iter (start from position 0 )
		rightCode= cal ( getInvEle( getCharCodeAt(s,iter) )  , rightCode);//remove iter
		if(leftCode == 1){//is i (for 0~iter)
			int subLeft  = 0; //empty
			int subRight = rightCode;

			for(long long iter2=iter+1 ; iter2<sMax-1 && iter2<biggestKposition ;++iter2){
				
				subLeft = cal( subLeft , getCharCodeAt(s,iter2));
				subRight= cal( getInvEle(getCharCodeAt(s,iter2)),subRight);
				if(subLeft==2 && subRight==3)return "YES";
			}
		}
	}

	return "NO";
}


int main(){
	int t;
	long long L,X;
	string s;
	cin>>t;
	for(int i = 0 ; i < t ; i++){
		cin>>L>>X>>s;
		cout<<"Case #"<<i+1<<": "<<execute(L,X,s)<<endl;
	}
	return 0;
}
