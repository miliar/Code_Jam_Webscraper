#include <iostream>
#include<fstream>
#include<string.h>

using namespace std;

int main()
{
    freopen("a1.in","r",stdin);
	freopen("a1.out","w",stdout);
	int t,j=0;
	cin>>t;
	for(int p=0;p<t;p++){

        string s,a;j=0;
        cin>>s;
  cout<<"Case #"<<p+1<<": ";
        a=s[0];
        for(int i=1;i<s.length();i++){
        if(s.at(j)>s.at(i)){
            a=a+s[i];

        }
        else if(s.at(j)<=s.at(i)){
                a=s[i]+a;
            j=i;

        }
        }
        cout<<a<<endl;


	}


    return 0;
}
