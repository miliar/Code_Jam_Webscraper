#include <iostream>
using namespace std;

int main() {
    freopen("A-large.txt","r",stdin);
    freopen("cj_1.txt","w",stdout);
	string str;
	int num,more,test,smax,i,total;
	cin>>test;
	for(int x=0;x<test;x++)
	{
	    num=0,more=0,total=0;
	    cin>>smax;
	    cin>>str;
	    for(i=0;i<str.length();i++)
	    {
	        if(num>=i)
	            num=num+(int)str[i]-48;
            else
            {
                more=i-num;
                num=num+(int)str[i]-48+more;
                total+=more;
            }
	    }
	    cout<<"Case #"<<x+1<<": "<<total<<endl;
	}
	return 0;
}
