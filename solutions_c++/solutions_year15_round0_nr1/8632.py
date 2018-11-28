/*
ID: guralbe1
PROG: test
LANG: C++             

#include<bits/stdc++.h>
*/
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

ifstream cin("file.in");
ofstream cout("file.out");

//vector<pair<int,int > >v;

//v.push_back(make_pair(a,b));
//vector < map <int, int> > v(sz)

int arr[1000009];
int main()
{
	string str;
	int n, current_ves, ans=0;
	int test;
	cin>>test;
	for(int t = 0; t < test;t ++ )
	{
		ans=0;
		cin>>n;
		current_ves=0;
		cin>>str;
		for(int i = 0; i <= n; i ++ )
		arr[i]=0;
		for(int i = 0; i <= n; i ++ )
		{
			arr[i]=str[i]-48;
	//		cout<<arr[i]<<" ";
		}
	//	cout<<endl;
		
			current_ves=arr[0];
		for(int i = 1; i <= n; i ++ )
		{
		//	cout<<"VEC " << current_ves<<endl;
			ans += max( 0 , i - current_ves );
			current_ves += max( 0 , i - current_ves );
			current_ves += arr[i];
		}
		//cout << "Vec " << current_ves << endl;
		cout << "Case #" << t+1 << ": " << ans << endl;
	
	}
	





return 0;
}

