#include <iostream>
using namespace std;

int main()
{
	freopen("B-small-attempt0.in","r",stdin); 
	freopen("output.out","w",stdout); 
	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++){
		int A,B,K;
		cin>>A>>B>>K;
		int count=0;
		for(int i=0;i<A;i++)
			for(int j=0;j<B;j++){
				if((i&j)<K)
					count++;
			}
		cout<<"Case #"<<cas<<": "<<count<<endl;
	}
    return 0;
}