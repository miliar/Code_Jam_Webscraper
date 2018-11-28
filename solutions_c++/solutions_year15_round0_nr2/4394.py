#include<bits/stdc++.h>
#include<set>
using namespace std;
multiset<int> st;
int ans(int d)
{
	if( *st.rbegin()<=2 || d==0 ) return *st.rbegin();
	int M = *st.rbegin();
	st.erase(st.find(M));
	int res = M;
	for(int i=1;i<=M/2;++i)
	{
		st.insert(i);
		st.insert(M-i);
		res = min( res , 1+ ans(d-1) );
		st.erase(st.find(i));
		st.erase(st.find(M-i));
	}
	st.insert(M);
	return res;
}
int main()
{
	#ifdef DBG
	freopen("B-small-attempt1.in", "r" , stdin);
	freopen("B-small-attempt1.out", "w" , stdout);
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
	int T,N,v,c=1;
	cin>>T;
	while(T--)
	{
		st.clear();
		cin>>N;
		while(N--)
		{
			cin>>v;
			st.insert(v);
		}
		cout<<"Case #"<<c++<<": "<<ans(*st.rbegin())<<endl;
	}

}

