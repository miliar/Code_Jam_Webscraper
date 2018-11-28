#include <iostream>
using namespace std;

int main() {
	int t,q;
	cin>>t;
	q=t;
	while(t>0)
	{
	    int k,c,s;
	    cin>>k>>c>>s;
	    cout<<"Case #"<<q-t+1<<": ";
	    for(int i=1;i<=k;i++)
	    cout<<i<<" ";
	    cout<<endl;
	    t--;
	}
	return 0;
}
