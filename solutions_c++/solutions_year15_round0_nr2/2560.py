#include <bits/stdc++.h>
using namespace std;

int main(){
	int nbTests;
	cin >> nbTests;
	for(int testNb = 1; testNb <= nbTests; testNb++){
		int nbDiners;
		cin >> nbDiners;
		priority_queue<int> diners;
		for(int i = 0; i < nbDiners; i++){
			int d;
			cin >> d;
			diners.push(d);
		}
		
		auto diners2 = diners;
		
		int min_time = 20000000;
		int cur_time = 0;
		while(true){
			//gewoon geen speciallekes meer
			min_time = min(cur_time + diners.top(), min_time);
			
			if(cur_time > min_time || diners.top() <= 1) break;
			
			//eens specialleke proberen
			int m = diners.top();
			diners.pop();
			diners.push(m/2 + m%2);
			diners.push(m/2);
			cur_time++;
		}
		
		cur_time = 0;
		diners = diners2;
		while(true){
			//gewoon geen speciallekes meer
			min_time = min(cur_time + diners.top(), min_time);
			
			if(cur_time > min_time || diners.top() <= 1) break;
			
			//eens specialleke proberen
			int m = diners.top();
			diners.pop();
			if(m%3 == 0 && m%2==1){
				diners.push(m/3);
				diners.push(m*2/3);
			}
			else{
				diners.push(m/2 + m%2);
				diners.push(m/2);
			}
			cur_time++;
			
		}
		
		cout << "Case #" << testNb << ": " << min_time << endl;
	}
	return 0;
}