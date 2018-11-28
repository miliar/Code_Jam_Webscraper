#include<cstdio>
#include<vector>
#include<list>
#include<algorithm>
using namespace std;
vector<char> vt;
list<char> li;
char A[1100];
int T;
int main(){
	
	freopen("A-large.in", "r", stdin);
	freopen("outputA.txt", "w", stdout);
	
	scanf("%d", &T);
	int t = 1;
	while (T--){
		scanf("%s", A);
		int i = 0;
		while (A[i]){
			if (li.empty())
				li.push_back(A[i]);
			else{
				if (li.front() > A[i])
					li.push_back(A[i]);
				else
					li.push_front(A[i]);
			}
			i++;
		}
		
		printf("Case #%d: ", t++);
		while (!li.empty()){
			printf("%c", li.front());
			li.pop_front();
		}
		printf("\n");
	}
}


