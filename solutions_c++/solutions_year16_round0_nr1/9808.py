#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef long long llint;

map<llint,llint> seen;

llint T;

bool insomina = false;
llint start;
llint times;


bool zerlege(llint x){
	llint t = 10;
	llint m = x%t;
	while(t < x){
		if(x%t == 0)seen[1]++;
		m = x%t;
		if(start != -1 && m == start){
			times++;
			if(times >= 300){
				insomina = true;
			}
		}
		x/=t;
		//cout << m << " ";
		seen[m]++;
		if(seen.size() == 10){
			return true;	
		}
	}
	m = x%t;
	seen[m]++;
	if(start != -1 && m == start){
		times++;
		if(times >= 300){
			insomina = true;
		}
	}
	//cout << m << "\n";
	if(seen.size() == 10){
			return true;	
	}
	return false;
}

int main(){
	cin >> T;
	for(int i=1;i<=T;i++){
		llint X;
		cin >> X;
		start = -1;
		insomina = false;
		times = 0;
		seen.clear();
		while(!zerlege(X)){
			if(start == -1)start = X;
			if(insomina){
				cout << "Case #" << i << ": INSOMNIA\n";
				break;
			}
			X += start;
		}
		if(!insomina){
			cout << "Case #" << i << ": " << X << "\n";
		}
	}
}
