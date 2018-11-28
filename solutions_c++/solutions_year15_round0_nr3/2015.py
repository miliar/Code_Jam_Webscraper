#include <iostream>
#include <vector>
#include <memory.h>
using namespace std;

int T, L;

bool fff[40005][40005];
char mul[128][128];
int sign[128][128];
long long X;

void init(){
	mul['1']['1'] = '1';
	mul['1']['i'] = 'i';
	mul['1']['j'] = 'j';
	mul['1']['k'] = 'k';
	sign['1']['1'] = 1;
	sign['1']['i'] = 1;
	sign['1']['j'] = 1;
	sign['1']['k'] = 1;
	
	mul['i']['1'] = 'i';
	mul['i']['i'] = '1';
	mul['i']['j'] = 'k';
	mul['i']['k'] = 'j';
	sign['i']['1'] = 1;
	sign['i']['i'] = -1;
	sign['i']['j'] = 1;
	sign['i']['k'] = -1;
	
	mul['j']['1'] = 'j';
	mul['j']['i'] = 'k';
	mul['j']['j'] = '1';
	mul['j']['k'] = 'i';
	sign['j']['1'] = 1;
	sign['j']['i'] = -1;
	sign['j']['j'] = -1;
	sign['j']['k'] = 1;
	
	mul['k']['1'] = 'k';
	mul['k']['i'] = 'j';
	mul['k']['j'] = 'i';
	mul['k']['k'] = '1';
	sign['k']['1'] = 1;
	sign['k']['i'] = 1;
	sign['k']['j'] = -1;
	sign['k']['k'] = -1;
}
int main(){
	cin >> T;
	string s;
	init();
	int count = 0;
	while(T--){
		cin >> L >> X;
		cin >> s;
		long long  left = 0, right = L * X - 1;
		long long leftM = (X < 4 ? X : 4) * L, rightM = ((X - 4) > 0 ? X - 4 : 0) * L;
		vector<long long> findi;
		vector<long long> findk;
		bool flag = false;
		char cur = '1';
		int si = 1;
		while(left < leftM){
			si *= sign[cur][s[left % L]];
			cur = mul[cur][s[left % L]];
			// find i
			if(cur == 'i' && si == 1)
				findi.push_back(left);
			left++;
		}
		cur = '1';
		si = 1;
		while(right >= rightM){
			si *= sign[s[right % L]][cur];
			cur = mul[s[right % L]][cur];
			// find k
			if(cur == 'k' && si == 1)
				findk.push_back(right);
			right--;
		}
		// cout << findi.size() << endl;
		// cout << findk.size() << endl;
		memset(fff, 0, sizeof(fff));
		for(int i = 1; i <= leftM; i++){
			cur = '1';
			si = 1;
			for(int j = 0; j < leftM; j++){
				si *= sign[cur][s[(i + j) % L]];
				cur = mul[cur][s[(i + j) % L]];
				if(cur == 'j' && si == 1){
					fff[i][j + 1] = true;
				}
			}
		}
		
		for(int i = 0; i < findi.size(); i++){
			for(int k = 0; k < findk.size(); k++){
				if(findk[k] <= findi[i])
					break;
				long long length = findk[k] - findi[i] - 1;
				length %= (4 * L);
				//cout << "fff" << findi[i] + 1 << "   " << length << endl;
				if(fff[findi[i] + 1][length]){
					flag = true;
					break;
				}
			}
			if(flag)
				break;
		}
		count++;
		if(flag)
			printf ("Case #%d: YES\n", count);
		else
			printf ("Case #%d: NO\n", count); 
	}
}