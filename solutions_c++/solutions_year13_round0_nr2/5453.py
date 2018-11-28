#include <iostream>

using namespace std;

unsigned char p[100][100];
int N, M;

void read(){
	cin >> N >> M;
	for(int i=0; i < N; i++){
		for(int j=0; j < M ; j++){
			cin >> p[i][j];
		}
	}
}

bool determine(){
	unsigned char max_r, max_c;
	for(int i=0; i<N ; i++){
		max_r=0;
		for(int j=0; j<M; j++) if(p[i][j] > max_r) max_r = p[i][j];
		
		for(int j=0; j<M; j++) if(p[i][j] < max_r){
			max_c=0;
			for(int z=0; z < N; z++) if(p[z][j] > max_c) max_c = p[z][j];
			
			for(int z=0; z < N; z++) if(p[z][j] < max_c) return false;
		}
	}
	return true;
}

int main(int argc, char** argv){
	int T;
	cin >> T;
	for(int n=1;n<=T;n++){
		read();
		cout<<"Case #"<< n <<": ";
		if(determine()) cout << "YES"<<endl;
		else cout << "NO"<<endl;
	}
	return 0;
}
