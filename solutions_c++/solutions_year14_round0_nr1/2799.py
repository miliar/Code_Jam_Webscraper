# include <iostream>
# include <cstdio>
# include <vector>
# include <string>
# include <queue>
# include <map>
# include <set>
# include <algorithm>
# include <sstream>
# include <fstream>
# include <cmath>

using namespace std;

// define values

# define INF 1<<30;

// variables goes here

int T,t,a1,a2,v;
int curr, card;

int main(){
	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("a.txt","w",stdout);

	cin>>T;
	
	while(T--){
		
		set<int> c;

		cin>>a1;

		for(int i = 1 ; i <= 4 ; i++){
			for(int j = 1 ; j <= 4 ; j++){
				cin>>v;
				if(i == a1) c.insert(v);
			}
		}

		curr = 4;
		cin>>a2;

		for(int i = 1 ; i <= 4 ; i++){
			for(int j = 1 ; j <= 4 ; j++){
				cin>>v;
				if(i == a2){
					c.insert(v);
					if(c.size() == curr)
						card = v;
					else curr = c.size();
				}
			}
		}

		cout<<"Case #"<<++t<<": ";

		if(c.size() == 8) cout<<"Volunteer cheated!";
		else if(c.size() < 7) cout<<"Bad magician!";
		else cout<<card;

		cout<<endl;
		
	}	
		
	return 0;
}















