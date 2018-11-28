#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdin(0);cin.tie(0);
using namespace std; int N, x;
int main(){cin >> N; for (int M=1; M<=N; M++){
	cin >> x; double arr[x];
	for (int i=0; i < x; i++){cin>>arr[i];}
	double art[x];
	for (int i=0; i < x; i++){cin>>art[i];} 
	cout << "Case #" << M << ": ";
	int str8=0;
	double ark[x];
	memcpy(ark,art,sizeof (art));
	sort(ark,ark+x);
	for (int i=0; i < x; i++){for (int j=0; j<x; j++){if(ark[j]>arr[i]){str8++; ark[j]=0; break;}}}
	sort(art,art+x);
	reverse(art,art+x);
	int mx=0;
	vector<double> v;
	for (int i=0;i<x;i++){v.push_back(arr[i]);} sort(v.begin(),v.end());reverse(v.begin(),v.end());
	for (int i=0;i<x;i++){
		int le=0;
		for(int j=0;j<x;j++){
			if(v[j]>art[j]){le++;}
			}
		v.insert(v.begin(),v[x-1]); 
		mx=max(mx,le);
	}
	cout << mx <<" "<<x-str8 << endl;
}return 0;}