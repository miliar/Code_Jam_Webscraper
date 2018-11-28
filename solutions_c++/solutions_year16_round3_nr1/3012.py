 #include <bits/stdc++.h>
using namespace std; 

#define endl '\n'
#define ll long long
#define input freopen("in.txt","r",stdin)
#define output freopen("out.txt","w",stdout)

int main(){ 

	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input;
	output;
	int t,n,k=1,may=-1,c,j,c0=0;
	string le="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	cin >> t;
	while(t--){
		c0=0,may-1;
		cout <<"Case #"<<k++<<": ";
		cin >> n;
		vector<int>v(n);
		for(int i=0;i<n;i++){
			cin >> v[i];
			if(v[i]>may)may=v[i];
		}
		while(true){
			c=(may==1 && (n-c0)==3)?1:2;
			c0=0;
			for(int i=0;i<n;i++){
				if(c==0)break;
				if(v[i]==may){
					cout <<le[i];
					v[i]--;
					c--;
					j=i;
				}
				if(v[i]==0)c0++;
			}
			if(c==1 && v[j]>0){
				cout <<le[j];
					v[j]--;
					c--;
				if(v[j]==0)c0++;	
			}
			may=-1;
			for(int i=0;i<n;i++)
				if(v[i]>may)may=v[i];
			if(may==0)break;
			cout <<" ";
		}
		cout << endl;
	}
}
