#include<iostream>
#include<string.h>
using namespace std;
int main(){
	int T;
	cin>>T;
	string s;
	for(int i=1;i<=T;i++)
	{
		cin>>s;
		int len=s.length();
		int count=0;
        char x = s[0];
        for(int j=0;j<len;j++){
             if(s[j]==x)
             continue;
             else
             {
                count++;
                x = s[j];
            }
        }
        count++;
        //for(int i=1;i<=len;i++){
            if(s[len-1]=='+')
              cout<<"case #"<<i<<": "<<count-1 <<endl;
           else
              cout<<"case #"<<i<<": "<<count<<endl;
      // }
	}
	return 0;
}
