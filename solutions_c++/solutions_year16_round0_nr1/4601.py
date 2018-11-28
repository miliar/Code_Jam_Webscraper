#include<bits/stdc++.h>
using namespace std;
bool arr[20];

bool chck(){
	for (int i = 0; i < 10; ++i)
	{
		if(arr[i]==false)return false;
	}
	return true;
}

int main(int argc, char const *argv[])
{
	freopen("input1large.in", "r", stdin);
	freopen("output1large.in", "w",stdout);
	int t, n, x, j, c, k;
	cin>>t;
	k=1;
	while(t--){
		cin>>n;
		if(n==0){
			cout<<"Case #"<<k<<": "<<"INSOMNIA\n";
			k++;
			continue;
		}
		j=0;
		memset(arr, false, sizeof(arr));
		while(!chck()){
			j++;
			x=n*j;
			while(x){
				c=x%10;
				arr[c]=true;
				x=x/10;
			}
		}
		x=n*j;
		cout<<"Case #"<<k<<": "<<x<<endl;
		k++;
	}
	return 0;
}