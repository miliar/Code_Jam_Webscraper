#include <bits/stdc++.h>

using namespace std;

int main(){
	int t, cases = 0;

	scanf("%d", &t);

	while(t--){
		cases++;
		vector<int> pq;
		int n, mi = 0, x;

		scanf("%d", &n);

		for(int i = 0; i < n; i++){
			scanf("%d", &x);

			pq.push_back(x);
		}

		sort(pq.begin(), pq.end());
		reverse(pq.begin(), pq.end());

		mi = pq[0];

		int cont = 1;

		while(cont < mi){
			int sum = 0;
			for(int i = 0; i < pq.size(); i++)
				sum += ((pq[i] - 1) / cont);
			sum += cont;
			mi = min(mi, sum);
			cont++;
		}

		printf("Case #%d: %d\n", cases, mi);
	}

	return 0;
}

/*int main(){
	int t, cases = 0;

	scanf("%d", &t);

	while(t--){
		cases++;
		priority_queue<int> pq;
		int n, cont = 0, mi = 0, x;

		scanf("%d", &n);

		for(int i = 0; i < n; i++){
			scanf("%d", &x);

			pq.push(x);
		}

		mi = pq.top();

		while(pq.top() > 1){
			cont++;			
			int a = pq.top();
			pq.pop();

			int l = a / 2;
			pq.push(l);
			if(a % 2 == 1)
				l++;
			pq.push(l);

			mi = min(mi, cont + pq.top());
		}

		mi = min(mi, cont + pq.top());

		printf("Case #%d: %d\n", cases, mi);
	}

	return 0;
}*/
