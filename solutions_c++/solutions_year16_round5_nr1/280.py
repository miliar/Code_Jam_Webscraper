#include<stdio.h>
#include<algorithm>
#include<vector>
#include<functional>
#include<string.h>
#define all(A) (A).begin(), (A).end()
#define II(A) int (A); scanf("%d",&(A));
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

const int LIM = 200000;

char buf[LIM];
int A[LIM];

int main(){
	freopen("input.txt","r",stdin),freopen("output.txt","w",stdout);
	int TC;
	scanf("%d",&TC);
	for(int tc=1;tc<=TC;tc++){
		scanf("%s",buf);
		int N = strlen(buf);
		vector<int> st;
		for(int i=0;i<N;i++){
			int pv = -1;
			if(buf[i]=='C') pv = 1;
			else pv = 2;

			if(!st.empty() && st.back() == pv){
				st.pop_back();
			}
			else{
				st.push_back(pv);
			}
		}
		int ans = 10*(N-st.size())/2 + 5*st.size()/2;
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}