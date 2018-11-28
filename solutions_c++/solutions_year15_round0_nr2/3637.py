#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int dp(priority_queue<int> pq, int minutes){
	if(pq.top() == 1 || pq.top() == 2 || pq.top() == 3){
		return minutes + pq.top();
	}
	priority_queue<int> pq1 = pq;
	int k = pq1.top();
	pq1.pop();
	pq1.push(k/2);
	//cout << k/2 << " " << k - k/2 << "\n"; 
	pq1.push(k - k/2);
    priority_queue<int> pq2;
    while(!pq.empty()){
		pq2.push(pq.top()-1);
		pq.pop();
	}
	//cout << min(dp(pq1, minutes+1), dp(pq2, minutes+1))<<endl;
	//cout << "Test \n";
	return min(
		   dp(pq1, minutes+1),
           dp(pq2, minutes+1)
			);
}

int getSum(vector<int> v, int it){
	int sum = 0;
	for(int i=0; i<v.size(); i++){
		sum += (v[i] - 1) / it;
	}
	return sum;
}

int main(){
	int t;
	cin >> t;
	for(int l=1;l<=t;l++){
		 //priority_queue<int> pq;
		 vector<int> v;
		 int n;
		 cin >> n;
		 while(n--){
			int temp;
			cin >> temp;
		   // cout << temp << " ";
		   // pq.push( temp );
			v.push_back(temp);
		 }
		 int ans, max = -1;
		 for(int i=0; i<v.size(); i++){
			if(max < v[i])
				max = v[i];
		 }
		 ans = max;
		 int it = 2;
		 while( it < ans ){
			//cout << ans << endl;
			ans = min(ans, getSum(v, it) + it);
			it++;
		 }
		 //cout << endl;
		// int minutes = 0;
		 cout <<"Case #"<<l<<": "<< ans <<endl;
	}
	return 0;
}
