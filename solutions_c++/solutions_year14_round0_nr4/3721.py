#include <fstream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

ifstream cin("test.in");
ofstream cout("test.out");

#define M 1010

int n;
double a[M],b[M];
set<double> bob;

void read(void){
	cin >> n;
	for (int i=0; i<n; ++i)
	cin>>a[i];
	for (int j=0; j<n; ++j)
	cin>>b[j];
	
	sort(a,a+n);
	sort(b,b+n);
	
	reverse(a,a+n);
	reverse(b,b+n);
}

void ini(void){
	for (int i=0; i<n; ++i)
	bob.insert(b[i]);
}

int get(double t){
	if (bob.lower_bound(t)!=bob.end()){
		bob.erase(bob.lower_bound(t));
		return 0;
	}
	bob.erase(bob.begin());
	return 1;
}

int get_deceitful(void){
	int ra=n-1,lb=0,rb=n-1, ans=0;
	while (ra>=0){
		if (a[ra]>b[rb]){
			++ans;
			--rb;
			--ra;
		}
		else{
			++lb;
			--ra;
		}
	}
	return ans;
}

int get_fair(void){
	int l = 0, r = n - 1, ans=0;
	for (int i=0; i<n; ++i)
	if (a[i]>b[l]){
		++ans;
		--r;
	}
	else
		++l;
	
	return ans;
}

void kill(void){ 
	cout<<get_deceitful()<<" "<<get_fair()<<"\n";
}


int main(){
	int t;
	cin>>t;
	
	cout.precision(8);
	cout<<fixed;
	
	for (int i=1; i<=t; ++i){
		cout<<"Case #"<<i<<": ";
		read();
		kill();
	}
	return 0;
}
