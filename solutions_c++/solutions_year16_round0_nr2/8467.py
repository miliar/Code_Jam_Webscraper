#include <bits/stdc++.h>
using namespace std;



int main() {
	// your code goes here
    freopen("input.txt","r",stdin);
    freopen("1.txt","w",stdout);
	long int t;
    cin>>t;
    while(t--)
        {
        string s;
        cin>>s;
        long int count=0;
        for(long int i=0;i<s.size()-1;i++)
            {
            if(s[i]!=s[i+1])
                count++;
            }
        if(s[s.size()-1]=='-')
            count++;
        cout<<count<<endl;
        }
	
	return 0;
}