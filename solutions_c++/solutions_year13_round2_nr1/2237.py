#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int finder(vector<int>d,int n,int a,int j){
	if(j>d.size()-1)
		return n;
	else{
		if(d[j]<a)
			return finder(d,n,a+d[j],j+1);
		else{
			int x=finder(d,n+1,a,j+1);
			int y=1231;
			if(a>1)
			y=finder(d,n+1,a+a-1,j);
			return min(x,y);
		}
	}
}
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n,a,l,in;
	cin>>n;
	
	for(int i=0;i<n;i++)
	{
		vector<int>data;
		cin>>a>>l;
		for(int j=0;j<l;j++)
		{
			int out=0;
			cin>>in;
			data.push_back(in);
		}
			sort(data.begin(),data.end());
			printf("Case #%i: %i\n",i+1,finder(data,0,a,0));
	}
	return 0;
}