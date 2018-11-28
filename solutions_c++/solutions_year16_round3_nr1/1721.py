#include <bits/stdc++.h>
#define pb push_back
#define pii pair <int, int>
#define mp make_pair
#define F first
#define S second
#define ll long long
#define iosbase ios_base::sync_with_stdio(false)
#define sc scanf
#define pr printf
#define null NULL
#define getcx getchar_unlocked
#define lb lower_bound
#define ub upper_bound
#define all(x) x.begin(), x.end()
#define pll pair<ll,ll>
#define vi vector <int>
#define vll vector <ll>
 
#define maxs 100005
#define logmaxs 35
 
#define MOD 1000000007
#define eps 1e-9
#define llmax 1e18+5
#define intmax 1e9+5
#define intmin -intmax
 
#define pi 3.14159265358979
 
using namespace std;

int a[30];

int main(){

	int t;
	cin>>t;

	for(int T=1; T<=t; T++){

		int n;
		cin>>n;

		priority_queue <pii> pq;

		for(int i=0; i<n; i++){
			cin>>a[i];
			pq.push(mp(a[i], i));
		}
		
		cout<<"Case #"<<T<<": ";

		while(!pq.empty()){
			
			if(pq.size()==2){
				pii x1,x2;
				x1=pq.top();
				pq.pop();

				x2=pq.top();
				pq.pop();

				if(x1.F==x2.F){
					for(int j=0; j<x1.F; j++){
						cout<<(char)(x1.S+'A')<<(char)(x2.S+'A')<<" ";
					}
					break;
				}
				else{
					pq.push(x1);
					pq.push(x2);
				}
			}

			pii x=pq.top();
			//cout<<x<<endl;
			pq.pop();
			
			int u,v;
			u=x.F;
			v=x.S;
			
			cout<<(char)(v+'A')<<" ";
			
			u--;
			
			if(u>0)
			pq.push(mp(u,v));
			
			
		}


		cout<<endl;
	}
	return 0;
}