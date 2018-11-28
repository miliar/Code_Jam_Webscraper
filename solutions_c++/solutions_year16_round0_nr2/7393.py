#include<bits/stdc++.h>
#define MX 100000
#define pb push_back
#define mp make_pair
#define fs first
#define sec second
#define sc scanf
#define pr printf
using namespace std;
int main(){
	int T,t,i,j,k,c,n;
	freopen("B-large.in","r",stdin);
	freopen("B-outputLarge.in","w",stdout);
	cin>>T;
	for(t=1;t<=T;++t){
		string s;
		stack<char> st;
        c=0;
        cin>>s;
       loop: n=s.length();
        int cnt=0;
        k=0;
        for(i=0;i<n;++i)
        {
        	if(s[i]=='-')
        		{
        			k=i;
        			++cnt;
        		}
        }
        if(cnt==0)
        	cout<<"Case #"<<t<<": "<<c<<"\n";
        else if(cnt==n)
        	cout<<"Case #"<<t<<": "<<c+1<<"\n";
        else if(cnt==1 && s[0]=='-')
        	cout<<"Case #"<<t<<": "<<c+1<<"\n";
        else if(cnt==1)
        	cout<<"Case #"<<t<<": "<<c+2<<"\n";
        else{
        	++c;
        	   i=0;
        	   while(s[i]=='+')
        	   {
        	   	s[i]='-';
        	   	++i;
        	   }
        	   if(i!=0)
        	   	++c;
               for(i=0;i<=k;++i){
               	if(s[i]=='+')
               		st.push('-');
               	else
               		st.push('+');
               }
              s="";
              while(!st.empty()) {
                char ch=st.top();
                s+=ch;
                st.pop();
              }
              goto loop;
        }
	}
	return 0;
}