#include <bits/stdc++.h>
using namespace std;

int main(){
int T;cin >>T;
for(int Case=0;Case<T;Case++){

ll N;cin >>N;
int A[N], ans1=0, ans2=0;
for(int i=0;i<N;i++)
{
	cin >> A[i];
	if(i>0)
		ans1+=max(A[i-1]-A[i],0);
		ans2=max(ans2,A[i-1]-A[i]);
}
ll ans3=0;
for(int i=0;i<N-1;i++){
	ans3+=min(ans2,A[i]);
}
	cout << "Case #"<<Case+1<<": "<<ans1<<" "<<ans3<<endl;


}}
