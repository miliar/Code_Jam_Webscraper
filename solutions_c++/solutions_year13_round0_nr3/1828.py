#include <cstdio>
#include <vector>

using namespace std;

int buf[30];
vector <long long> v;

int main(){// freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int n;
	for(long long i=1; i<=10000000; i++){
		long long t;
		int id;
		bool f = 1;
		
		t = 1; 
		id = 0;
		while( i>=t ){
			buf[id++] = (i/t)%10;
			t *= 10;
		}

		for(int j=0; j<id; j++)
			if(buf[j] != buf[id-1-j])
				f = 0;
		if(f){
			t = 1;
			id = 0;
			while( i*i>=t ){
				buf[id++] = ((i*i)/t)%10;
				t *= 10;
			}
			for(int j=0; j<id; j++)
				if(buf[j] != buf[id-1-j])
					f = 0;
		}


		if(f){
			v.push_back(i*i);
		//	printf("%llu (%llu)\n", i, i*i);
		}
	}
	
	int T, si = v.size();
	scanf("%d", &T);

	long long A, B;
	for(int r=1; r<=T; r++){
		int ret = 0;
		scanf("%lld %lld", &A, &B);
		for(int i=0; i<si; i++)
			if(A <= v[i] && v[i] <= B)
				ret ++;
		printf("Case #%d: %d\n", r, ret);
	}


}