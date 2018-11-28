#include <iostream>
#include<string>
using namespace std;

int main() {
	int T,j=1;
	cin>>T;
	while(j<=T)
	{
	    string S;
	    string O;
	    char ch;
	    cin>>S;
	    O.push_back(S[0]);
	    for(int i=1;i<S.length();i++)
	    {
	        ch=O[0];
	        if(S[i]<O[0])
	        {
	           O.push_back(S[i]);
	        }
	        else
	        {
	            string T;
	            T.push_back(S[i]);
	            T+=O;
	            O.assign(T);
	          
	        }
	    }
	    cout<<"Case #"<<j<<": "<<O<<'\n';
	    j++;
	}
	return 0;
}