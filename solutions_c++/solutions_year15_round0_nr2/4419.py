#include <iostream>
#include <string>
#include <vector>
#include <queue>
using namespace std;

int T, t, op;

int d, tmp, minmin;
priority_queue<int> p;

void GetMinimum(priority_queue<int> P, int minutes){

	if (P.top() < 4){
		minmin = minutes+P.top() < minmin ? minutes+P.top() : minmin;
		return;
	}

	int x, y;
	priority_queue<int> newP, bu = P;

	x = bu.top();
	bu.pop();

	if (x == 9){
		priority_queue<int> newBu = bu;
		//y = x / 3; 
		newBu.push(3);
		newBu.push(6);
		GetMinimum(newBu, minutes + 1);
	}
	y = x / 2;
	bu.push(y);
	bu.push(y + x % 2);
	GetMinimum(bu, minutes + 1);


	while (P.size()){
		x = P.top() - 1;
		P.pop();
		if (!x)
			continue;
		newP.push(x);
	}
	GetMinimum(newP, minutes + 1);


}


int main(){

	freopen("ip.in", "r", stdin);
	freopen("op.txt", "w", stdout);

	cin >> T;	t = T;

	for(int t=1 ; t<=T ; t++){

		while (p.size())
			p.pop();
		minmin = INT_MAX;

		cin >> d;
		for (int i = 0; i < d; i++)
		{
			cin >> tmp;
			p.push(tmp);
		}

		GetMinimum(p, 0);

		op = minmin;

		printf("Case #%d: %d\n", t, op);
	}


	return 0;
}