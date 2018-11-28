#include <bits/stdc++.h>
using namespace std;

int main() {

	int t;
	cin>>t;
	int r=1;
//freopen("new.txt","w",stdout);
	while(t--){



	    string s;
	    cin>>s;
	    char a=s[0];
	    string h="";
	    h=h+a;
	    int l=s.length();
	    int i;
	    for(i=1;i<l;i++){

	        if(s[i]>=a){

	            h=s[i]+h;

	            a=s[i];
	        }
	        else
	        h=h+s[i];


	    }

	        cout<<"Case "<<"#"<<r<<": "<<h<<endl;
	        r++;
	    }
//fclose(stdout);



	return 0;
}
