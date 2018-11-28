#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <sstream>

using namespace std;

string X[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int R[10]={8,3,0,4,5,6,7,9,1,2};
char D[10][5];
int ND[10];
map<char,int>DV[10];

string ItoS(int x)
{
	stringstream SS;
	SS<<x;
	return SS.str();
}

int main(int argc, char** argv) {
	int T,k,i,n,N,L; string S;
	for(i=0;i<10;i++)
		{	n=0;
			N=X[i].size();
			map<char,int>DM;
			for(k=0;k<N;k++)if(!DM.count(X[i][k]))
								{DM[X[i][k]]=1; D[i][n++]=X[i][k];}
								else DM[X[i][k]]++;
			DV[i]=DM; ND[i]=n;
		}
	//for(i=0;i<10;i++)cout<<ND[i]<<' '; cout<<endl;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>T;
	for(k=1;k<=T;k++)
	{vector<int>ans(10,0);
	 cin>>S;
	 int j;
	 N=S.size();
	 int M[256]={0};
	 for(i=0;i<N;i++)
	 M[S[i]]++;
	 //for(char L='A';L<='Z';L++)cout<<k<<' '<<L<<M[L]<<' '; cout<<endl;
	 for(L=0;L<10;L++)
	 	{ i=R[L];
	 	  for(j=0;j<ND[i];j++)
		   if(DV[i][D[i][j]]>M[D[i][j]])break;
		  if(j<ND[i])continue;
		  ans[i]++;
		  for(j=0;j<ND[i];j++)
		  	M[D[i][j]]-=DV[i][D[i][j]];
		  L--;		
		}
	 cout<<"Case #"<<k<<": ";
	 for(L=0;L<10;L++)while(ans[L]--)cout<<L;
	 cout<<endl;
	 //for(char L='A';L<='Z';L++)cout<<k<<' '<<L<<M[L]<<' '; cout<<endl;	
	}
	
	return 0;
}
