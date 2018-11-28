#include <deque>
#include <cstdio>

#include <iostream>
#include <sstream>

using namespace std;



int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int i, j, t;
	cin >> t;
	//scanf("%d", &t);
	string pal;
	deque<char> est;
	for(i = 1; i <= t; i++){
		est.clear();
		cin >> pal;
		est.push_front(pal[0]);
		for(j = 1; j < pal.size(); j++){
			if(est.front() <= pal[j]){
				est.push_front(pal[j]);
			}else{
				est.push_back(pal[j]);
			}
		}
		cout << "Case #" << i << ": "; 
		while(!est.empty()){
			cout << est.front();
			est.pop_front();
		}cout << endl;
		
		//printf("Case #%d: \n", i);
		

		
		
	}

	return 0;
}