#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,k,sum;
	cin>>T;
	for(k=1;k<=T;k++)
	{int N,i,sum=0;
	 cin>>N;
	 vector<int>V(N);
	 vector<pair<int,int> >D(N);
	 for(i=0;i<N;i++){
	  cin>>V[i]; sum+=V[i];
	  D[i]=make_pair(V[i],i);
	 }
	 //for(i=0;i<N;i++)cout<<" "<<V[i]; cout<<endl;
	 sort(D.begin(),D.end());
	 cout<<"Case #"<<k<<":";
	 while(sum)
	 {  N=D.size();
	 	if(sum>4){
	 		cout<<' '<<(char)(D[N-1].second+'A')<<(char)(D[N-2].second+'A');
				D[N-1].first--; D[N-2].first--;
				sum-=2;
		 }
		else if(sum==3){
			 cout<<' '<<(char)(D[N-1].second+'A'); sum--; D[N-1].first--;
			 }
		else if(sum==4){
			if(D[N-1].first>2 || D[N-1].first==2 && D[N-2].first==1){
				cout<<' '<<(char)(D[N-1].second+'A')<<(char)(D[N-1].second+'A');
				D[N-1].first-=2;
			} else {
				cout<<' '<<(char)(D[N-1].second+'A')<<(char)(D[N-2].second+'A');
				D[N-1].first--; D[N-2].first--;
			}
			sum-=2;	
		}
			else {
			if(D[N-1].first>=2){
				cout<<' '<<(char)(D[N-1].second+'A')<<(char)(D[N-1].second+'A');
				D[N-1].first-=2;
			}
			else {
				cout<<' '<<(char)(D[N-1].second+'A')<<(char)(D[N-2].second+'A');
				D[N-1].first--; D[N-2].first--;
			}
	 		sum-=2;
			}
		//for(i=0;i<N;i++)
		//	cout<<" ["<<D[i].second<<"] "<<D[i].first<<" ";
		//cout<<endl<<endl;
		 sort(D.begin(),D.end());
	 }
	 cout<<endl;	 
	}
	return 0;
}
