#include <iostream>
using namespace std;

int main() {
	int T, N, i, j;
	char a[1002];
	cin>>T;
	for(i=1; i<=T; ++i)
	{
	    cin>>N>>a;
	    int count=0, s[1001]={0};
	    s[0]=a[0]-'0';
	    for(j=1; j<=N; ++j)
	    {
	        if(s[j-1]<j && a[j]!='0')
	        {
	            count+=(j-s[j-1]);
	            s[j]=j+a[j]-'0';
	        }
	        else
	            s[j]=s[j-1]+a[j]-'0';
	    }
	    cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}
