#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<list>
#include<queue>
#include<set>
#include<stack>
#include<cmath>
#include<algorithm>
#include<functional>
using namespace std;

int visit[100];
int T;
char A[3000];
string ans;
int result[100];
//vector<int> ans;
void find(){
	if (visit['Z' - 'A'] > 0 && visit['E' - 'A']>0 && visit['R' - 'A'] >0 && visit['O' - 'A']>0){
		result[0]++;
			//ans += '0';
			visit['Z' - 'A']--;
			visit['E' - 'A']--;
			visit['R' - 'A']--;
			visit['O' - 'A']--;
			find();
		}



	else if (visit['W' - 'A'] > 0 && visit['T' - 'A']>0 && visit['O' - 'A']>0){
		result[2]++;
		//ans += '2';
			visit['T' - 'A']--;
			visit['W' - 'A']--;
			visit['O' - 'A']--;
			find();
		}

	else if (visit['F' - 'A'] > 0 && visit['O' - 'A'] > 0 && visit['R' - 'A'] >0 && visit['U' - 'A']>0){
		result[4]++;
		visit['F' - 'A']--;
		visit['O' - 'A']--;
		visit['R' - 'A']--;
		visit['U' - 'A']--;
		find();
	}


	else if (visit['X' - 'A'] > 0 && visit['S' - 'A']>0 && visit['I' - 'A']>0){
		result[6]++;
		visit['S' - 'A']--;
		visit['I' - 'A']--;
		visit['X' - 'A']--;
		find();
	}
	else if (visit['T' - 'A'] > 0 && visit['H' - 'A'] > 0 && visit['R' - 'A'] > 0 && visit['E' - 'A'] >1){
		result[3]++;
		visit['R' - 'A']--;
		visit['T' - 'A']--;
		visit['H' - 'A']--;
		visit['E' - 'A'] -= 2;
		find();
	}
	else if (visit['S' - 'A'] > 0 && visit['E' - 'A'] > 1 && visit['V' - 'A'] > 0 && visit['N' - 'A'] > 0){
		result[7]++;
		visit['S' - 'A']--;
		visit['E' - 'A'] -= 2;
		visit['V' - 'A']--;
		visit['N' - 'A']--;
		find();
	}
	else if (visit['E' - 'A'] > 0 && visit['I' - 'A'] > 0 && visit['G' - 'A'] > 0 && visit['H' - 'A'] >0 && visit['T' - 'A']>0){
		result[8]++;
		visit['I' - 'A']--;
		visit['G' - 'A']--;
		visit['E' - 'A']--;
		visit['H' - 'A']--;
		visit['T' - 'A']--;
		find();
	}



	else if (visit['F' - 'A'] > 0 && visit['I' - 'A'] > 0 && visit['V' - 'A']>0 && visit['E' - 'A']>0){
		result[5]++;
		visit['F' - 'A']--;
		visit['I' - 'A']--;
		visit['V' - 'A']--;
		visit['E' - 'A']--;
		find();
	}

	else if (visit['N' - 'A'] > 1 && visit['I' - 'A'] > 0 && visit['E'-'A'] > 0){
		result[9]++;
		visit['N' - 'A'] -= 2;
		visit['I' - 'A']--;
		visit['E' - 'A']--;
		find();
	}

	else if (visit['O' - 'A'] > 0 && visit['N' - 'A'] > 0 && visit['E' - 'A'] > 0){
		result[1]++;
		visit['O' - 'A']--;
		visit['N' - 'A']--;
		visit['E' - 'A']--;
		find();
	}
}
int main(){
	
	freopen("A-large.in", "r", stdin);
	freopen("outputA.txt", "w", stdout);
	
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%s", A);
		int k = 0;
		memset(visit, 0, sizeof(visit));		memset(result, 0, sizeof(result));
		ans.clear();
		while (A[k] != 0){
			visit[A[k] - 'A']++;
			k++;
		}

		find();
		for (int i = 0; i < 10; i++){
			while (result[i] > 0){
				ans += (i + '0');
				result[i]--;
			}
		}
		printf("Case #%d: %s\n",i, ans.c_str());
	}
}


