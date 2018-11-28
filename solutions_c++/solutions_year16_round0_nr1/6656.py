#include <bits/stdc++.h>

using namespace std;

bool visited[10];
int result;

void init() {
	memset(visited, 0, sizeof(visited));
}

void visitnum(int num) {
	while(num) {
		visited[num%10]=true;
		num/=10;
	}
}

bool needsToVisit() {
	for (int i=0;i<10;i++) {
		if (!visited[i]) return true;
	}
	
	return false;
}

int main(void)
{
	ios::sync_with_stdio(false);

	int T;
	int tcase = 0;
	cin>>T;
	string answer;
	
	while (++tcase<=T) {
		init();
		
		int num;
		cin>>num;
		
		result = num;
		
		while (num&&needsToVisit()) {
			visitnum(result);
			
			result+=num;
		}
		result-=num;
		
		cout<<"Case #"<<tcase<<": ";
		
		if (num==0) {
			cout<<"INSOMNIA";	
		} else {
			cout<<result;
		}
		
		cout<<endl;
	}
	
	return 0;
}

