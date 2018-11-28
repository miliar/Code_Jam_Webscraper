#include <iostream>
#include <cstring>

using namespace std;
int a[16],b[16];
int check(int n1,int n2);
int main(int argc, char const *argv[])
{
	int T;
	int n1,n2;
	cin >> T;
	for(int cn = 1; cn <= T; cn++){
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		cin >> n1;
		for(int i=0;i<16;i++){
			cin >> a[i];
		}
		cin >> n2;
		for(int i=0;i<16;i++){
			cin >> b[i];
		}
		int rt = check(n1,n2);	
		cout << "Case #" << cn << ": ";
		if(rt == -1) cout << "Bad magician!";
		else if(rt == 0) cout << "Volunteer cheated!";
		else cout << rt;
		cout << endl;
	}
	return 0;
}
int check(int n1,int n2){
	int res = 0;
	for(int i = (n1-1)*4+0; i < (n1-1)*4+4; i++){
		for(int j= (n2-1)*4+0; j < (n2-1)*4+4; j++){
			if(a[i] == b[j]){	
				if(res == 0){
					res = a[i];
				}else if(res > 0){
					res = -1;
					return res;
				}
			}
		}
	}
	return res;
}