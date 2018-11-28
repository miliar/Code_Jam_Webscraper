#include <cstdio>
#include <vector>

using namespace std;


int main(){
	int t;
	scanf("%d",&t);
	for (int i=0; i<t; i++){
		int n;
		char c;
		scanf("%d",&n);
		scanf("%c",&c);
		vector<int>A;
		for (int j=0; j<n+1; j++){
			scanf("%c",&c);
			int num = c - '0';
			A.push_back(num);
		}
		//for(int j=0; j<A.size(); j++) printf("%d ",A[j]);
		//printf("\n");

		int newfriend = 0;
		int people = 0;

		for (int j=0; j<A.size(); j++){
			if (A[j] == 0) continue;
			if (j > people){
                newfriend += j - people;
                people += newfriend;
			}
			people += A[j];
		}
		printf("Case #%d: %d\n", i+1, newfriend);
	}
}
