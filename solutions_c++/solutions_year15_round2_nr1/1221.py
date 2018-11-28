#include <stdio.h>
#include <string.h>
#include <queue>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

long long rev (long long n){
	long long cur = 0;

	while (n){
		cur *= 10LL;
		cur += n%10LL;
		n /= 10LL;
	}

	return cur;
}

int main (){
	
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt","w",stdout);
	
	int t;
	scanf ("%d", &t);

	for (int tc=1;tc<=t;tc++){
		
		long long n;
		scanf ("%lld", &n);

		queue <long long> q;
		map <long long, long long> mp;
		mp.clear();

		q.push(1LL);
		mp[1] = 1;

		while (!q.empty()){
			long long c = q.front();
			q.pop();

			//cout << c << endl;
			if (c == n){
				printf ("Case #%d: %lld\n", tc, mp[c]);
				break;
			}


			int nn = c+1;
			if (mp.find(nn) == mp.end()){
				mp[nn] = mp[c]+1;
				q.push(nn);
			}

			if (nn == n){
				printf ("Case #%d: %lld\n", tc, mp[nn]);
				break;
			}
			
			nn = rev(c);
			if (nn && mp.find(nn) == mp.end()){
				mp[nn] = mp[c]+1;
				q.push(nn);
			}

			if (nn == n){
				printf ("Case #%d: %lld\n", tc, mp[nn]);
				break;
			}
		}
	}
	return 0;
}
