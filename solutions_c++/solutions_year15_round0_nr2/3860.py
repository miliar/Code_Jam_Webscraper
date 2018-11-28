#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
int result;
int maxvalue;
bool compare_nocase (const int first, const int second){
	return first > second;
}

void func(const priority_queue< int, vector<int>, less<int> >& q, int cutValue,int maxValue){
	
	if(result > cutValue + maxValue){
		result = cutValue + maxValue;
	}

	if( q.top() < 4){
		return;
	}
	
	int mCake = q.top();
	
	for(int i = 2 ; i <= mCake/2; i++){
		
		priority_queue< int, vector<int>, less<int> > q2 = q;
		//cout<<q2.top();
		q2.pop();
		q2.push(i);
		q2.push(mCake -i);
		func(q2,cutValue+1,q2.top());
	}
}

int main(){
	int t;
	cin >> t;
	int k = 1;
	
	while(t--){
		int d;
		cin >> d;
		result = 0;
		priority_queue< int, vector<int>, less<int> > q; 

		for(int i = 0 ; i < d ; i++	){
			int value;
			cin >> value;
			q.push(value);
			if(result < value){
				result = value;
			}
		}
		
		maxvalue = result;
		
		func(q,0,maxvalue);
		cout<< "Case #"<<k<<": "<< result <<endl;
		k++;
	}
	return 0;

}