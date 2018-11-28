#include <iostream>
using namespace std;
bool memo[10000][10000][2];
string word;
int L, X;
char prod[108][108];
int sign[108][108];

bool K(int ii, int xx){
	char act = '1';
	int sig = 1;

	for(int i=ii+1;i<L;i++){
		sig *= sign[act][word[i]];
		act = prod[act][word[i]];
		if(memo[i][xx][1])
			return false;
		memo[i][xx][1] = true;
	}

	for(int x=xx+1;x<X;x++){
		for(int i=0;i<L;i++){
			sig *= sign[act][word[i]];
			act = prod[act][word[i]];
			if(memo[i][x][1])
				return false;
			memo[i][x][1] = true;
		}
	}

	if(act == 'k' && sig ==1)
		return true;

	return false;
}

bool JK(int ii, int xx){
	char act = '1';
	int sig = 1;

	for(int i=ii+1;i<L;i++){
		sig *= sign[act][word[i]];
		act = prod[act][word[i]];
		if(act == 'j' && sig == 1  && K(i,xx)){
			return true;
		}
		if(memo[i][xx][0])
			return false;
		memo[i][xx][0] = true;


	}


	for(int x=xx+1;x<X;x++){
		for(int i=0;i<L;i++){
			sig *= sign[act][word[i]];
			act = prod[act][word[i]];
			if(act == 'j' && sig == 1  && K(i,x)){
				return true;
			}
			if(memo[i][x][0])
				return false;
			memo[i][x][0] = true;
		}
	}


	return false;
}
int main(){
	prod[49][49]=prod[105][105]=prod[106][106]=prod[107][107]='1';
	prod[49][105]=prod[105][49]=prod[106][107]=prod[107][106]='i';
	prod[49][106]=prod[105][107]=prod[106][49]=prod[107][105]='j';
	prod[49][107]=prod[105][106]=prod[106][105]=prod[107][49]='k';

	sign[49][49]=sign[49][105]=sign[49][106]=sign[49][107]=sign[105][49]=sign[105][106]=sign[106][49]=sign[106][107]=sign[107][49]=sign[107][105]=1;
	sign[105][105]=sign[105][107]=sign[106][105]=sign[106][106]=sign[107][106]=sign[107][107]=-1;


	int T;
	cin >> T;
	for(int caso=1; caso<T+1; caso++){
		bool canBeBroken = false;
		cin >> L >> X;
		for(int i=0;i<L;i++)
			for(int j=0;j<X;j++)
				memo[i][j][0] = memo[i][j][1] = false;
		cin >> word;
		char act = '1';
		int sig = 1;
		for(int x=0;x<X;x++){
			for(int i=0;i<L;i++){
				sig *= sign[act][word[i]];
				act = prod[act][word[i]];
				//si es i y sig = 1 getCrazy;
				if(act == 'i' && sig == 1  && JK(i,x)){
					canBeBroken=true;
					break;
				}
			}
			if(canBeBroken)
				break;
		}
		cout << "Case #" << caso << ": ";
		if(canBeBroken)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
}