#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

#define		MAX		1000
#define		NUM		32
#define		P		168


int n,c;
int isprime[MAX];
vector<int> prime;
int mod[11][NUM][P];
int res[11];

int main(){

	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	memset(isprime,true,sizeof(isprime));
	isprime[1] = false;
	isprime[2] = true;
	for (int i=2;i<MAX;i++){
		if (isprime[i]){
			prime.push_back(i);
			for (int j=i;j<MAX;j+=i){
				isprime[j] = false;
			}
		}			
	}

	//cout << prime.size() << endl;
	//return 0;

	for (int i=2;i<=10;i++){
		for (int k=0;k<P;k++){
			int pr = prime[k];
			mod[i][0][k] = 1;
			for (int j=1;j<NUM;j++){
				mod[i][j][k] = (mod[i][j-1][k]*i)%pr;
			}
		}
	}

	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> n >> n;
		cout << "Case #" << tc << ":" << endl;		
		string s;
		for (int i=0;i<NUM-2;i++) s+= "0";
		for (int i=1;i<NUM-2 && n;i++){
			string p = s;
			for (int k=0;k<i;k++) p[NUM-2-k-1] = '1';
			do{
				bool find = false;
				for (int d=2;d<=10;d++){					
					find = false;
					for (int k=0;k<P;k++){
						int pr = prime[k];
						int r = 1+mod[d][NUM-1][k];
						for (int a=NUM-3;a>=0;a--)
							r += (p[a]=='1')?mod[d][NUM-3-a+1][k]:0;
						if (r % pr == 0){
							res[d] = pr;
							find = true;
							break;
						}
					}
					if (!find) break;
				}
				if (find){
					cout << 1 << p << 1;
					for (int k=2;k<=10;k++) cout << " " << res[k];
					cout << endl;
					n--;
					if (!n)
						break;
				}
			}while(next_permutation(&p[0],&p[0]+NUM-2));
		}
	}

	return 0;
}