#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>

#define F(i, n) for(i = 0;i < n; ++i)
#define pb(a, b) a.push_back(b)
#define li long int

using namespace std;

struct node
{
	char c;
	li fre;
};

vector <struct node> a[124];
vector <li> sum;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	li n, t, i, j, cnt = 0;
	cin >> t;
	while(t--){
		li ans = 0;
		string temp;
		cin >> n;
		cout << "Case #" << ++cnt << ": ";
		F(j, n){
			i = 0;
			cin >> temp;
			while(i < temp.size()){
				struct node b;
				li cur = 1;
				while(i < temp.size() && temp[i] == temp[i + 1]){
					++i;
					++cur;
				}
				b.fre = cur;
				b.c = temp[i];
				pb(a[j], b);
				++i;
			}
		}
		F(i, n){
			F(j, a[i].size()){
		//		cout << a[i][j].c << " " << a[i][j].fre << " ";
			}
		//	cout << "\n";
		}	
		F(i, n){
			if(a[i].size() != a[0].size()) break;
		}
		if(i != n){
			sum.clear();
			F(i, 124){
				a[i].clear();
			}
			cout << "Fegla Won\n";
			continue;
		}
		F(j, a[0].size()){
			li cur = 0;
			F(i, n){
				if(a[i][j].c != a[0][j].c) break;
				cur += a[i][j].fre; 
			}
			if(i != n) break;
			cur = round(  (double)cur / n );
			pb(sum, cur);
		}
		if(j != a[0].size()){
		 	sum.clear();
			F(i, 124){
				a[i].clear();
			}
		 	cout << "Fegla Won\n";
		 	continue;
		}
		
		F(j, a[0].size()){
		//	cout << sum[j] << " ";
			F(i, n){
				ans += abs(a[i][j].fre - sum[j]);
			}
		}
		//cout << "\n";
		cout << ans << "\n";
		sum.clear();
		F(i, 124){
			a[i].clear();
		}
	}
	return 0;
}
