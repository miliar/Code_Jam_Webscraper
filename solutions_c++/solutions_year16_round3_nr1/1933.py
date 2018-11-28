#include <cstdio>
#include <queue>

using namespace std;

class Cnt {
public:
	Cnt(int n, int cnt) : _n(n), _cnt(cnt) {}
	bool operator < (const Cnt& rhs) const { return _cnt < rhs._cnt; }
	int _n, _cnt;
};

int main(void){
	priority_queue<Cnt> q;
	int T,t;
	int N;
	int i, cnt, sum;
	scanf("%d", &T);
	for(t=0;t<T;t++)
	{
		scanf("%d",&N);
		q = priority_queue <Cnt> ();
		sum=0;
		for(i=0;i<N;i++) {
			scanf("%d", &cnt);
			q.push( Cnt(i, cnt) );
			sum+=cnt;
		}
		printf("Case #%d: ",(t+1));
		while(true) {
			Cnt tmp = q.top();
			q.pop();
			printf("%c", 65+tmp._n);
			
			tmp._cnt--;
			sum--;
			if(sum == 0)	break;

			q.push(tmp);

			tmp = q.top();
			q.pop();
			Cnt tmp2 = q.top();
			if((sum-1) < tmp2._cnt * 2){
				q.push(tmp);
				printf(" ");
				continue;
			}
			printf("%c ", 65+tmp._n);

			tmp._cnt--;
			sum--;
			if(sum == 0)	break;
	
			q.push(tmp);			
			
		}
		printf("\n");
	} 
}
