#include<map> 
#include<set>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int n;

	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> n;
		vector<pair<int,char> > p(n);

		for (int i=0;i<n;i++){
			cin >> p[i].first;
			p[i].second = 'A'+i;
		}

		sort(p.begin(),p.end());
		reverse(p.begin(),p.end());

		cout << "Case #" << tc << ": ";

		int k = 1;
		while(k!=n){
			while(k<n && p[k].first==p[k-1].first) k++;
			int d;
			if (k==n) d=p[k-1].first;
			else d = p[k-1].first-p[k].first;
			if (k%2 == 0){
				for (int c=0;c<d;c++){
					for (int i=0;i<k;i+=2){
						p[i].first--;
						p[i+1].first--;
						cout << p[i].second << p[i+1].second << " ";
					}
				}				
			}
			else{
				int c = d/2;
				while(c--){ 
					p[k-1].first-=2;
					cout << p[k-1].second << p[k-1].second << " ";
				}
				if (d&1){ 
					p[k-1].first--;
					cout << p[k-1].second << " ";
				}

				for (int c=0;c<d;c++){
					for (int i=0;i<k-1;i+=2){
						p[i].first--;
						p[i+1].first--;
						cout << p[i].second << p[i+1].second << " ";
					}
				}				
			}
		}

		cout << endl;
	}

	return 0;
}