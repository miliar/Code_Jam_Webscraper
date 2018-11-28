#include <iostream>
#include <map>
#include <set>


using namespace std;


int main(int argc, char *argv[]) {
	
	freopen("input.txt","r",stdin);
	freopen("fle.txt","w",stdout);
	
	int tc; cin >> tc;
	int test=1;
	int arr[4][4];
	
	while(tc--) {
		set <int> st;
		int first ; cin >> first;
		int second ;
		for(int i=0 ; i<4 ; i++) for(int j=0 ; j<4; j++) cin >> arr[i][j];
		
		for(int i=0 ; i<4 ; i++) st.insert(arr[first-1][i]);
		
		cin >> second;
		for(int i=0 ; i<4 ; i++) for(int j=0 ; j<4; j++) cin >> arr[i][j];
		
		
		int cnt=0;
		int ans;
		for(int i=0 ; i<4 ; i++) {
			for(set<int>::iterator it=st.begin() ; it != st.end() ; it++) {
				if(*it == arr[second-1][i]) {
					cnt++;
					ans = arr[second-1][i];
					break;
				}
			}
		}
		
		if(cnt == 0) {
			printf("Case #%d: Volunteer cheated!",test++);
		}
		else if(cnt == 1) {
			printf("Case #%d: %d",test++,ans);
		}
		else {
			printf("Case #%d: Bad magician!",test++);
		}
		puts("");
	}	
	return 0;
}