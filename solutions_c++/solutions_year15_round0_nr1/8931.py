#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
int main()
{
   int T;
   cin>>T;
   cin.ignore();
   for(int cases=1;cases<=T;cases++)
   {
   	int smax,ret=0,standing=0;
	string s;
    	cin>>smax>>s;
	standing=s[0]-'0';
	for(int i=1;i<=smax;i++) {
		int shynum=i;
	//	cout<<"shynum = "<<shynum<<" standing = "<<standing<<" retint = "<<ret;
		if(standing >= shynum || (s[i]-'0')==0)
			standing+=(s[i]-'0');
		else {
			//6 0400051
			ret+=(shynum-standing);
			standing+=(s[i]-'0')+(shynum-standing);
		}
	//	cout<<" retafter = "<<ret<<endl;
	}
    	cout<<"Case #"<<cases<<": "<<ret<<endl;
   }
    

    return 0;
}
