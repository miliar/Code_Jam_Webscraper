#include <iostream>
#include <vector>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
	    string s;
	    cin>>s;
	    for(int j=1;j<s.length();j++)
	    {
	        vector<char> s1;
	        if(s[j]-'A'>=s[0]-'A')
	        {
	            s1.push_back(s[j]);
	            for(int k=0;k<j;k++) s1.push_back(s[k]);
	            for(int p=0;p<s1.size();p++) s[p]=s1[p];
	        }
	    }
	    cout<<"Case #"<<i+1<<": "<<s<<endl;
	}
	return 0;
}