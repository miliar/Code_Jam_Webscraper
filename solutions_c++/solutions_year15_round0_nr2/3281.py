#include <iostream>
#include <set>
#include <algorithm>
#include <math.h>

//YOLO
//code by loyolman

using namespace std;

int pancakes[1047];//how many people have number[i] pancakes

int main() {
	int T;
	cin>>T;
	
	for (int j=0;j<T;j++) {
		int D;//dick :)
		int best_time=99999;
		int time;
		for (int i=0;i<1047;i++) pancakes[i]=0;
		
		cin>>D;
		for (int k=0;k<D;k++) {
			int h;
			cin>>h;
			pancakes[h]++;
		}
		
		for (int i=1;i<1046;i++) {
			time=0;
			for (int j=i+1;j<1046;j++) {
				int h=(j/i)-1;
				if (j%i>0) h++;
				//break down one man with j pancakes to pancakes with size up to i takes h time
				time+=h*pancakes[j];
			}
			best_time=min(best_time, i+time);
		}
		
		cout<<"Case #"<<j+1<<": "<<best_time<<endl;
	}
}
