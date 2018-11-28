#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class q_union{
	private:
	int *id,*sz,size;
	int root(int i){
		while(i != id[i]){
			id[i] = id[id[i]];
			i = id[i];
		}
		return i;
	}
	
	public:
		q_union(int N){
			id = new int[N],size = N;
			sz = new int[N];
			for(int i = 0; i <= N; i++){
				sz[i] = 1;
				id[i] = i;
			}
			
		}
		bool find(int p , int q){
			return root(p) == root(q);
		}
		void unite(int p,int q){
			int x = root(p);
			int y = root(q);
			if(sz[x] > sz[y]){
				id[x] = y;
				sz[y] += sz[x];
			}
			else{
				id[y] = x;
				sz[x] += sz[y];
			}
		}
		void print(int N){
			cout << "i     ";
			for(int i = 0; i <= N; i++){
				cout << i << " ";  
			}
			cout << endl;
			cout << "id[i] ";
			for(int i = 0; i <= N; i++){
				cout << id[i] << " ";  
			}
			cout << endl;
			cout << "sz[i] ";
			for(int i = 0; i <= N; i++){
				cout << sz[i] << " ";  
			}
			cout << endl;
		}
};
int main(){
	
	int tc;
	cin >> tc;
	bool fr = false;
	for(int i = 1; i <= tc; i++){
		if(fr){
			cout << endl;
		}
		int n;
		cin >> n;
		int tmp = n;
		int ori = n;
		int counter = 0;
		q_union un(11);
		if(n <= 0){
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}
		int x = 1;
		while(counter < 10){
			tmp = ori*x;
			n = tmp;
			//cout << "tmp : " << tmp << endl;
			while(n > 0){
				int d = n%10;
				n /= 10;
			//	cout << "digit : " << d << endl;
				if(!un.find(11,d)){
					un.unite(11,d);
				//	cout << "join" << 11 << " and " << d << endl;
					counter++;
				}
			}
			
		//	cout << "counter : "<< counter << endl;
			x++;
		}

			cout << "Case #" << i << ": "<< tmp;

			
		fr=true;
	}
	
	
	return 0;
}
