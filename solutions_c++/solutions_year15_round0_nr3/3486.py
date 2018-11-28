#include <iostream>

using namespace std;

void resolve(int caseNum);
int tranform(int mul1,int mul2);
int trans2(char a);
int sign1(int mul1,int mul2);
int main(){
	
	int testCase;
	cin >> testCase;

	for(int i=0; i<testCase; i++)
		resolve(i+1);
	

	return 0;
}

void resolve(int caseNum){
	long long L;
	long long X;
	string str;
	int sign=1;
	int mul=0;
	int result = 0;

	cin >> L >> X;
	cin >> str;

	for( long long i=0; i<X; i++){
		for( long long j=0; j<L; j++){
			sign *= sign1(mul,trans2(str[j]));
			mul = tranform(mul,trans2(str[j]));
			
			if( result == 0 ){
				if( mul==1 && sign ==1)
					result++;
			}
			if( result == 1 )
				if( mul==3 && sign ==1)
					result++;
			
		}
	}
	if( result == 2 )
		if( mul==0 && sign==-1)
			result++;

	if( result==3)
		cout << "Case #" << caseNum << ": YES"<<endl;
	else
		cout << "Case #" << caseNum << ": NO" <<endl;
}
int tranform(int mul1, int mul2){
	
	int trans[4][4] = { {0,1,2,3},{1,0,3,2},{2,3,0,1},{3,2,1,0}};
	return trans[mul1][mul2];	

}
int trans2(char a){
	if( a=='i')
		return 1;
	else if( a=='j')
		return 2;
	else 
		return 3;
}
int sign1(int mul1, int mul2){
	int trans[4][4] = {{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};

	return trans[mul1][mul2];
}
