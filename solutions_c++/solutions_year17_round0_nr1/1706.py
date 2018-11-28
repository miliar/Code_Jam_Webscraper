#include <iostream>
#include <cassert>

using namespace std;

void flip(string &S,const int d,const int K)
{
    for(int i=d; i<d+K; i++)
	S[i]^=('+'^'-');
}

void test(int cse)
{
    cout<<"Case #"<<cse<<": ";
    string S; cin>>S; int K; cin>>K;
    int n=0;
    for(int d=0; d<S.size(); d++) {
	if(S[d]=='+')
	    continue;
	if(d+K>S.size()) {
	    cout<<"IMPOSSIBLE\n";
	    return;
	}
	flip(S,d,K);
	n++;
    }
    cout<<n<<endl;
}

int main()
{
    int T; cin>>T;
    for(int i=0; i<T; i++)
	test(i+1);
    return 0;
}
