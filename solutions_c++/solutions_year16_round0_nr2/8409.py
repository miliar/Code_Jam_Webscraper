#include<bits/stdc++.h>
using namespace std;
typedef pair<char, int> pci;
int tcs;
char buf[105];
stack<pci> pff;
int main(){
	scanf("%i\n", &tcs);
	for(int tc=1;tc<=tcs;tc++){
		gets(buf);
		while(!pff.empty()){pff.pop();}
		for(int i=0;i<strlen(buf);i++){
			if(pff.size() == 0 || pff.top().first != buf[i]) pff.push(pci(buf[i], 1));
			else pff.top().second++;
		}
		pci last; int ct = 0;
		while(!pff.empty()){
			last = pff.top();
			pff.pop();
			if(last.first == '-') ct += 2;
		}
		if(last.first == '-') ct--;
		printf("Case #%i: %i\n", tc, ct);
	}
}