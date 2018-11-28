


#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>
#include <climits>


const double Pi = acos(-1.0);
typedef long long LL;

#define Set(a, s) memset(a, s, sizeof (a))
#define Rd(r) freopen(r, "r", stdin)
#define Wt(w) freopen(w, "w", stdout)

using namespace std;

int main(){
	Rd("A-small-attempt0.in");
	Wt("answers.out");
	int t;
	cin>>t;
	for(int n=1;n<=t;n++){
		int row1[4];
		int board1[4][4];
		int answer1;
		cin>>answer1;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>board1[i][j];
			}
		}
		for(int i=0;i<4;i++){
			row1[i]=board1[answer1-1][i];
		}
		int answer2;
		cin>>answer2;
		int board2[4][4];
		int row2[4];
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin>>board2[i][j];
			}
		}
		for(int i=0;i<4;i++){
			row2[i]=board2[answer2-1][i];
		}

		vector<int> matches;
		for(int i=0;i<4;i++){
			int n1=row1[i];
			for(int j=0;j<4;j++){
				int n2=row2[j];
				if(n1==n2)
					matches.push_back(n1);
			}
		}
		//testing section

		/*cout<<"row1: ";
		for(int i=0;i<4;i++){
			cout<<row1[i];
		}
		cout<<endl<<"row2: ";
		for(int i=0;i<4;i++){
			cout<<row2[i];
		}
		cout<<endl;*/

		if(matches.size()==1){
			vector<int>::iterator ii = matches.begin();
			cout<<"Case #"<<n<<": "<<*(ii)<<endl;
		}
		else if(matches.size()==0){
			cout<<"Case #"<<n<<": "<<"Volunteer cheated!"<<endl;
		}
		else if(matches.size()>1){
			cout<<"Case #"<<n<<": "<<"Bad magician!"<<endl;
		}

	}
	return 0;
}
