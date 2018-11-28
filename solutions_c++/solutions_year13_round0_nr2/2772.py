#include<iostream>
using namespace std;
struct PA
{
	int x,y,s;
	bool operator<(const PA&t)const
	{
		return s<t.s;
	}
};
int main()
{
	int A[100][100];
	bool B[100][100];
	int T;
	int idx=0;
	cin >> T;
	while(T--)
	{
		++idx;
		int N,M;
		cin >> N >> M;
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j)
				cin >> A[i][j];
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j)
				B[i][j] = false;
		for(int i=0;i<N;++i)
		{
			bool is1=true;
			for(int j=0;j<M;++j)
				if(A[i][j]==2)is1=false;
			if(is1)
			for(int j=0;j<M;++j)
				B[i][j] = true;
		}
		for(int j=0;j<M;++j)
		{
			bool is1=true;
			for(int i=0;i<N;++i)
				if(A[i][j]==2)is1=false;
			if(is1)
			for(int i=0;i<N;++i)
				B[i][j] = true;
		}
		bool ans = true;
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j)
				if(A[i][j]==1 && B[i][j]==false)
					ans=false;
		cout << "Case #"<<idx<<": ";
		if(ans)cout<<"YES"<<endl;
		else cout <<"NO"<<endl;
	}
}
