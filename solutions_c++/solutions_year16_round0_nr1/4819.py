#include <fstream>
#include <cstring>

using namespace std;

ifstream cin("A-large.in");
ofstream cout("sheep.out");

long long N,T,rs,a[10],o;
bool u;

void check(int n)
{
	int k;
	while(n>0)
	{
		k=n%10;
		if (!a[k]) a[k]=1;
		n/=10;
	//	cout<<k<<" "<<n<<endl;
	}
 } 
 
 int main(){
 	cin>>T;
 	 for(int i=1; i<=T; ++i)
 	 {
 	 	cin>>N;
 	 	if(N==0) cout<<"case #"<<i<<": INSOMNIA"<<endl;
 	 	else
		{
 	 	u=1;
 	 	 for(int j=0; j<10; ++j)
 	 	   a[j]=0;
 	 	 for(int j=1; u;++j )
 	 	 {
 	 	 	for(o=0; o<10 && a[o]; ++o);
 	 	 	if(o<10)check(j*N);
 	 	 	else
			{
 	 	 	    cout<<"case #"<<i<<": "<<(j-1)*N<<endl;
 	 	 	    u=0;
 	 	    }
		 }
	    }
	  }
 }
