#include <iostream>
#include <vector>
#include <string>
#include<map>
#include <unordered_map>
#include <fstream>
#include <istream>
#include <ostream>
#include <sstream>
#include<set>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include<queue>

using namespace std;
class S{
public:
char name;
int val;

};

struct L
{
  bool operator()(const S& lhs, const S& rhs) const
  {
    return lhs.val < rhs.val;
  }
};


int main(){

int T,t = 0;

cin >> T;

while(t < T){
		int N,n=0, tsum = 0;
		cin >> N;
		vector<S> P(N);
		priority_queue<S,std::vector<S>,L> pq,temp;
		while(n < N){
			cin >> P[n].val;
			P[n].name = 'A' + n;
			tsum += P[n].val;
			pq.push(P[n]);
			n++;
		}
		
		cout << "Case #" << t+1 << ": "; 
		while(!pq.empty()){
			S a = pq.top();
			pq.pop();
			a.val--;
			tsum--;
			if(a.val > 0){
				pq.push(a);
			}
			S b;
			b.val = -1;
			if(!pq.empty() && tsum != 2){
				b = pq.top();
				pq.pop();
				b.val--;
				tsum--;
				if(b.val > 0){
					pq.push(b);
				}
			}
			if(b.val != -1){
				cout << a.name << b.name << " ";
			}else {
				cout << a.name << " ";
			}
		}
		
		cout << endl;
		t++;
	}

return 1;
}
