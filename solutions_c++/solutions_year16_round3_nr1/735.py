#include <iostream>

#include <deque>
#include <stdio.h>
using namespace std;
 
int n, p[40], pt;
deque< pair<int,int> > plan;
 
bool search_plaaan2 (int i1, int i2){
	bool ansss2= false;
 
	plan.push_back(make_pair(i1,i2));
	p[i1]--; pt--;
	if (i2 != -1){
		p[i2]--; pt --;
	}
 
	if ((p[i1] < 0) || (i2 != -1 && p[i2] < 0))
		goto check_ans1;
 
 	for (int i=0; i<n; i++)
 		if (p[i] > pt/2) goto check_ans1;
 
	if (pt == 0)
		ansss2 = true;
	else {
		for (int i=0; i<n && !ansss2; i++)
		for (int j=-1; j<n && !ansss2; j++)
				ansss2 = search_plaaan2(i, j);
	}
 
	check_ans1:
	if (ansss2 == false){
		plan.pop_back();
		p[i1]++; pt++;
		if (i2 != -1){
			p[i2]++; pt++;
		}
	}
 
	return ansss2;
}
 
int main(){
	int t;
	bool ans;
 
	scanf ("%d", &t);
 
	for (int k=1; k<=t; k++){
		scanf ("%d", &n);
 
		pt = 0;
		for (int i=0; i<n; i++){
			scanf ("%d", &p[i]);
			pt += p[i];
		}
 
		plan.clear();
 
		ans = false;
		for (int i=0; i<n && !ans; i++)
			for (int j=-1; j<n && !ans; j++)
				ans = search_plaaan2 (i, j);
 
		printf ("Case #%d:", k);
 
		while (!plan.empty()){
			pair<int,int> next = plan.front();
			int i1 = next.first, i2 = next.second;
 
			printf (" %c", i1+'A');
			if (i2 != -1)
				printf ("%c", i2+'A');
 
			plan.pop_front();
		}
 
		printf ("\n");
	}
 
	return 0;
}