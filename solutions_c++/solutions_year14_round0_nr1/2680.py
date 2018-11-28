#include <climits>
#include <iostream>
#include <vector>

using namespace std;

void  testcase(int casex){
	int row;
	vector<int> tab(17,0);
	int w,x,y,z;
	cin >>row;
	for(int i=1; i<=4; i++){
		cin >>w>>x>>y>>z;
		if(i==row){
		tab[w]++;
		tab[x]++;
		tab[y]++;
		tab[z]++;
		}
	}
	cin >>row;	
	for(int i=1; i<=4; i++){
		cin >>w>>x>>y>>z;
		if(i==row){
		tab[w]++;
		tab[x]++;
		tab[y]++;
		tab[z]++;
		}
	}
	int res =-1;
	for (int i=1; i<17;i++){
		if(tab[i]==2){
			if(res ==-1) res =i;
			else res = -2;
		}
	}
	cout << "Case #"<<casex<<": ";
	if(res ==-1) cout <<"Volunteer cheated!"<<endl;
	else if(res ==-2) cout <<"Bad magician!"<<endl;
	else cout <<res<<endl;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int cases;
	cin >> cases;
	for(int i =1; i<=cases;i++){
		testcase(i);  
	}

  return 0;
}
