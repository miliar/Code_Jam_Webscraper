#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

long long F(int m,int P)
{
	long long res=0,D=1;
	for(;m;m>>=1)
		{
			res+=D*(m&1);
			D*=P;
		}
	return res;
}

int main() 
{
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int T,n; 
	cin>>T;
	for(n=1;n<=T;n++)
	{int N,J,P,m; long long M,i;
	 cin>>N>>J;
	 m=1|(1<<N-1); m-=2;
	 //for(P=2;P<=10;P++)
	 //	cout<<F(m,P)<<" ";
	 //cout<<endl;
	 cout<<"Case #"<<n<<":"<<endl;
	 while(J)
	 {	m+=2;
	 	//cout<<m<<" "<<F(m,10)<<endl;
	 	vector<long long>V(10);
	 	for(i=3;i*i<=m;i+=2)
	 		if(m%i==0){V[1]=i;break;}
	 	if(i*i>m)continue;
	 	for(P=3;P<=10;P++)
	 		{
	 			M=F(m,P);
	 			if(!(M & 1)){V[P-1]=2; continue;}
	 			for(i=3;i*i<=M;i+=2)
	 				if(M%i==0){V[P-1]=i;break;}
				if(i*i>M)break;	
			 }
		if(P<=10)continue;
		V[0]=M;
		//cout<<F(m,10)<<" ";
		cout<<V[0];
		for(i=1;i<10;i++)cout<<" "<<V[i];
		cout<<endl;
		J--;
	 }
	 
	}
	
	return 0;
}
