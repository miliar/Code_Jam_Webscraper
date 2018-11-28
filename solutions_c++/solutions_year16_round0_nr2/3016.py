    /*sourav verma(Swerve7)   IPG_2013108  ABV IIITM
         Task @ Google Code Jam */
    
#include<bits/stdc++.h>
#define ll  long long int
using namespace std;

int main()
{
    int tc;cin>>tc;
    for(int i=1;i<=tc;i++){
        char s[200]; cin>>s;
		ll y=0;
		if(s[0]=='-') y=1;
		for(int i=1;s[i]!='\0';i++) {
			if((s[i]=='-') && (s[i-1]=='+'))
			    y+=2;
		} 
        cout<<"Case #"<<i<<": "<<y<<"\n";
    }
    return 0;
}