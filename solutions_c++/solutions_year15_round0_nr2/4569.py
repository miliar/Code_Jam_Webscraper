#include <iostream>
#include <stdio.h>
using namespace std;

struct table{
	int arr[200] = {};
	int D;

};

void gogo(table* target, int time);

bool isfinish(table* target){
	for (int i = 0; i < target->D; i++){
		if (target->arr[i] > 0){
			return false;
		}
	}
	return true;
}

void copy(table* co, table* ori){

	co->D = ori->D;
	for (int i = 0; i < ori->D; i++){
		co->arr[i] = ori->arr[i];
	}

}
void turn1(table* target,int time){
	int max = 0;
	int maxi = -1;
	for (int i = 0; i < target->D; i++){
		if (target->arr[i] > max){
			max = target->arr[i];
			maxi = i;
		}
	}
	
	if (max > 2){
		int half = max / 2;
	
		for (int j = half; j < max; j++){
			table co4;
			copy(&co4, target);
			co4.arr[maxi] = j;
			co4.arr[co4.D++] = max - j;
			gogo(&co4, time + 1);
		}
	}	
}

void turn2(table* target,int time){
	for (int i = 0; i < target->D; i++){
		target->arr[i]--;
	}

	gogo(target,time + 1);
}

int ans = 9999;

void gogo(table* target,int time){
	//cout << "d" << time << endl;
	if (isfinish(target)){

		if (time < ans){
			ans = time;
		}
		return;
	}
	if (time > ans){
		return;
	}
	
	table co1;
	copy(&co1, target);
	turn1(&co1, time);
		
	table co2; 
	copy(&co2, target);
	turn2(&co2, time);
	
}

int main(){
	freopen("B-small-attempt4.in", "r", stdin);
	freopen("B-small-attempt4.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		
		table roottable;
		cin >> roottable.D;
		for (int i = 0; i < roottable.D; i++){
			int k;
			cin >> k;
		
			roottable.arr[i] = k;
		}
		ans = 9999;
		gogo(&roottable, 0);
		
		cout << "Case #" << t << ": " << ans << endl;

	}

	return 0;
}