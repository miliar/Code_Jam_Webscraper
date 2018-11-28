#include<bits/stdc++.h>
#define ll long long int 
#define user hardik
#define ld long double
#define mod 1000000007
using namespace std;
 
int n, p[1000], pt;
deque< pair<int,int> > plan;
 
bool func(int i1, int i2){
	bool ans = false;
 
	plan.push_back(make_pair(i1,i2));
	p[i1]--; pt--;
	if (i2 != -1){
		p[i2]--; pt --;
	}
 
	if ((p[i1] < 0) || (i2 != -1 && p[i2] < 0))
		goto lol;
 	
 	for (int i=0; i<n; i++)
 		if (p[i] > pt/2) goto lol;
 
	if (pt == 0)
		ans = true;
	else {
		for (int i=0; i<n && !ans; i++)
			for (int j=-1; j<n && !ans; j++)
				ans = func (i, j);
	}
 
	lol:
	if (ans == false){
		plan.pop_back();
		p[i1]++; pt++;
		if (i2 != -1){
			p[i2]++; pt++;
		}
	}
 
	return ans;
}
 
int main()
{
 	ios_base::sync_with_stdio(0);
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
				ans = func(i, j);
 
		printf ("Case #%d:", k);
       ll kk=0;
		while (!plan.empty()){
			pair<int,int> next = plan.front();
			int i1 = next.first, i2 = next.second;
kk++;
 
			printf (" %c", i1+'A');
			if (i2 != -1)
				printf ("%c", i2+'A');
 //cout<<kk<<endl;
			plan.pop_front();
		}
 ////////////////////////////////newline
		printf ("\n");
	}
 
	return 0;
}