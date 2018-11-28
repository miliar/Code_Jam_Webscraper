#include<iostream>
#include<cstdio>
#include<vector>
#include<set>
using namespace std;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for(int u=1;u<=T;++u){
		int N,M;
		cin>>N>>M;
		set<int> s;
		int A[N][M];
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j){
				cin>>A[i][j];
				if(s.find(A[i][j])==s.end())
					s.insert(A[i][j]);
			}
		int curstr[N],curstol[M];
		
		for(int i=0;i<N;++i){
			curstr[i]=A[i][0];
			for(int j=1;j<M;++j){
				if(A[i][j]!=curstr[i])
					curstr[i]=0;
			}
		}
		for(int i=0;i<M;++i){
			curstol[i]=A[0][i];
			for(int j=1;j<N;++j){
				if(A[j][i]!=curstol[i])
					curstol[i]=0;
			}
		}
		/*for(int i=0;i<N;++i)
		cout<<curstr[i]<<" ";
		cout<<endl<<endl;
		for(int i=0;i<M;++i)
		cout<<curstol[i]<<" ";
		cout<<endl<<endl;*/
		bool iscool=true;
		for(int t=0;t<s.size()-1;++t){
			int q=*s.begin();
			s.erase(q);
			int l=*s.begin();
			for(int i=0;i<N;++i){
				for(int j=0;j<M;++j){
					if(A[i][j]==q)
					{
						//cout<<"c"<<i<<" "<<j<<" "<<curstr[i]<<" "<<curstol[j]<<" "<<A[i][j]<<endl;
						if(curstr[i]==A[i][j]||curstol[j]==A[i][j])
						{
						}
						else {
							iscool =false;
						}
						A[i][j]=l;
					}
				}
			}
			/*for(int i=0;i<N;++i){
				for(int j=0;j<M;++j)
				cout<<A[i][j]<<" ";
				cout<<endl;
			}*/
			for(int i=0;i<N;++i){
			curstr[i]=A[i][0];
			for(int j=1;j<M;++j){
				if(A[i][j]!=curstr[i])
					curstr[i]=0;
			}
		}
		for(int i=0;i<M;++i){
			curstol[i]=A[0][i];
			for(int j=1;j<N;++j){
				if(A[j][i]!=curstol[j])
					curstol[i]=0;
			}
		}
		}
		cout<<"Case #"<<u<<": ";
		if(iscool)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
		
	}
	return 0;
}
