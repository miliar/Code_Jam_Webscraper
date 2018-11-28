#include <iostream>
#include <sstream>
#include <math.h>
#include <assert.h>
#include <vector>

using namespace std;

int main(){

	freopen("q3.txt", "r", stdin);
	freopen("q3.out", "w", stdout);

	int cases;
	cin>>cases;

	for(int i=0;i<cases;i++){
		int r, c, m;
		cin>>r>>c>>m;
		int n, m_, k;

		n = r;
		m_ = c;
		k = m;

		//cout<<"Case #"<<i+1<<": "<<r<<" "<<c<<" "<<m<<endl;

		cout<<"Case #"<<i+1<<": ";
		vector<vector<char>> v(r, vector<char>(c, '*'));

		if(n == 1 || m_ == 1 || n == 2 || m_ == 2){
			cout<<k<<endl;
			continue;
		}

		if(n*m_ == k){
			cout<<(n+m_)*2-4<<endl;
			continue;
		}

		if(k == 1){
			cout<<1<<endl;
			continue;
		}

		if(k == 2){
			cout<<2<<endl;
			continue;
		}

		if(k == 3){
			cout<<3<<endl;
			continue;
		}

		if(k == 4){
			cout<<4<<endl;
			continue;
		}

		int ex = 3;
		int sq;
		int free = m+3;
		int free_ = free + 3;

		if(free > r*c){
			free = r*c;
			ex = free - m;
		}

		sq = ceil(sqrt((double)free));

		int hor, ver;
		
		if(sq >= c){
			ver = c;
			hor = free/c;
			if(free%c != 0)
				hor++;
		}
		else if(sq >= r){
			hor = r;
			ver = free/r;
			if(free%r != 0)
				ver++;
		}
		else{
			ver = sq;
			hor = sq;
		}

		bool do_ = false;
		if(free == ver*(hor-1)+1 || free == hor*(ver-1)+1)
			do_ = true;

		//if(free != r*c){
			/*if (free == 1){
				cout<<"Impossible"<<endl;
				continue;
			}*/

			/*if((free == 3 || free == 2) && r!=1 && c!=1){
				cout<<"Impossible"<<endl;
				continue;
			}*/
		//}

		for(int j=0;j<r;j++){
			for(int k=0;k<c;k++){
				if(j==0 && k==0){
					v[j][k] = 'c'; free--; continue;
				}
				if(j < hor && k < ver && free > 0){
					if(free == 2 && do_ && m>0 && ver>1 && hor>1 && k==ver-1){
						v[j][k] = '*';
						m--;
						continue;
					}
					v[j][k] = '.';
					free--;
				}
				else{
					v[j][k] = '*';
					m--;
				}
			}
		}

		int count = 0;
		v[0][0] = '.';

		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(v[i][j] == '*'){
					if(i > 0){
						if(v[i-1][j] == '.')
							v[i-1][j] = 1;
					}
					if(j > 0){
						if(v[i][j-1] == '.')
							v[i][j-1] = 1;
					}
				}
			}
		}

		int i, j;

		for(i=0;i<r;i++){
			if(v[i][0] == '.')
				v[i][0] = 1;
		}

		for(j=0;j<c;j++){
			if(v[0][j] == '.')
				v[0][j] = 1;
		}
		int j_, i_;
		for(j_ = 0;j_<c;j_++){
			if(v[i-1][j_]=='.' || v[i-1][j_]==1)
				v[i-1][j_] = 1;
			else
				break;
		}

		for(i_ = 0;i_<r;i_++){
			if(v[i_][j-1]=='.' || v[i_][j-1]==1)
				v[i_][j-1] = 1;
			else
				break;
		}

		if(sqrt((double)free) > (int)sqrt((double)free)){
		if(j_ < c && j_ > 2){
			if(i-3>-1){
			if(v[i-3][j_] != 1)
				count--;
			}
		}

		if(i_ < r && i_ > 2){
			if(j-3>-1){
			if(v[i_][j-3] != 1)
				count--;
			}
		}
		}

		for(i=0;i<r;i++){
			for(j=0;j<c;j++){
				if(v[i][j]==1)
					count++;
			}
		}



		cout<<count-ex<<endl;
		//if(m != 0)
		//	cout<<"err"<<endl;

		//for(int j=0;j<r;j++){
		//	int sum = 0;
		//	for(int k=0;k<c;k++){
		//		if(v[j][k] == '.' || v[j][k] == 'c')
		//			sum++;
		//	}

		//	if(sum == 1 && c>1 && free_ != 1){
		//		cout<<"Impossible"<<endl;
		//		goto ext;
		//	}
		//}

		//for(int k=0;k<c;k++){
		//	int sum = 0;
		//	for(int j=0;j<r;j++){
		//		if(v[j][k] == '.' || v[j][k] == 'c')
		//			sum++;
		//	}

		//	if(sum == 1 && r>1 && free_ != 1){
		//		cout<<"Impossible"<<endl;
		//		goto ext;
		//	}
		//}

		/*for(int j=0;j<r;j++){
			for(int k=0;k<c;k++){
				cout<<v[j][k];
			}
			cout<<endl;
		}*/

ext:
		;
	}
	return 0;
}