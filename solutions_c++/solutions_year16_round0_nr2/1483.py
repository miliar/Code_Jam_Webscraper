#include <iostream>
#define ll long long int
using namespace std;

int main() {
	// your code goes here
	int t;
	char c[101];
	cin>>t;
	for(int x =1;x<=t;x++)
	{
	    cin>>c;
	    int i=-1;
	    int count=0;
	    bool isP=(c[0]=='-');
	    bool isP0=(c[0]=='+');
	    while(c[++i])
	    {
	        if((c[i]=='+' && isP==0)||(c[i]=='-' && isP))
	        {
	            isP=!isP;
	            count++;
	        }
	            
	    }
	   // cout<<isP0<<"  "<<(count&1)<<"  "<<count<<endl;
	   cout<<"Case #"<<x<<": ";
	    cout<<(((isP0 && (count&1))||(!isP0 && !(count&1)))?(count-1):count)<<endl;
	}
	return 0;
}

