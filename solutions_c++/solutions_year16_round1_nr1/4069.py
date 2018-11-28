#include <bits/stdc++.h>
using namespace std;

int main() {

	int T;
	cin>>T;
	int x=1,i=0;
  
	for(i=0;i<T;i++)
  {
	    string s;
	    cin>>s;
	    char a=s[0];
	    string y="";
	    y=y+a;
	    int len=s.length();
	    int j;
	    for(j=1;j<len;j++)
      {
	        if(s[j]>=a){
	            y=s[j]+y;
	            a=s[j];
	        }
	        else
	        y=y+s[j];

	    }
	        cout<<"Case "<<"#"<<x<<": "<<y<<endl;
	        x++;
	    }
  
	return 0;
}
