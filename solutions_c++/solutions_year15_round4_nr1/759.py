#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 0x3f3f3f3f
#define MEMSET_INF 127
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

char b[101][101];

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)	{
		int r,c;
		cin >> r >> c;
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				cin >> b[i][j];
			}
		}

		bool imp = false;

		int count = 0;
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(b[i][j] != '.')	{

					bool ok = false;
					for(int k = 0; k < r; k++){
						if(k == i)
							continue;
						if(b[k][j] != '.'){
							ok = true;
							break;
						}
					}

					for(int k = 0; k < c; k++){
						if(k == j)
							continue;
						if(b[i][k] != '.'){
							ok = true;
							break;
						}
					}

					if(!ok){
						imp = true;
						break;
					}

					ok = false;
					if(b[i][j] == '<')	{
						for(int k = 0;  k<j; k++){
							if(b[i][k] != '.')	{
								ok = true;	
								break;
							}
						}
					}else if(b[i][j] == '>'){
						for(int k = j+1;  k<c; k++){
							if(b[i][k] != '.')	{
								ok = true;	
								break;
							}
						}
					}else if(b[i][j] == '^'){
						for(int k = 0;  k<i; k++){
							if(b[k][j] != '.')	{
								ok = true;	
								break;
							}
						}
					}else if(b[i][j] == 'v'){
						for(int k = i+1;  k<r; k++){
							if(b[k][j] != '.')	{
								ok = true;	
								break;
							}
						}
					}

					if(!ok){
						count++;
					}
				}
			}
			if(imp){
				break;
			}
		}

		cout << "Case #" << t << ": ";
		if(imp){
			cout << "IMPOSSIBLE" << endl;
		}else{
			cout << count << endl;
		}
	}
    return 0;
}