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

# define INF 1<<30;

int T,t,a;
double C,F,X,mini,curr,rate;

int main(){
	
	freopen("B-large.in","r",stdin);
	freopen("binputlarge.txt","w",stdout);
	cout.precision(7);
	cout.setf(ios::fixed,ios::floatfield);

	cin>>T;
	
	while(T--){

		cout<<"Case #"<<++t<<": ";
		cin>>C>>F>>X;

		rate = 0.5;
		mini = INF;
		a = 1;

		curr = X/2;

		while(true){
			if(curr > mini) break;
			mini = curr;
			curr = C*rate + X/(2+(a)*F);
			rate += 1/(2+a*F);
			a++;
		}
		cout<<mini<<endl;
		
	}	
		
	return 0;
}















