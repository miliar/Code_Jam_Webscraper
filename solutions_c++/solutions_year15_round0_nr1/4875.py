#include<iostream>
#include<string>

using namespace std;

int main()
{
    int T;
    cin>>T;
    for (int i=0;i<T;i++)
    {
	int sm,j,v,out,m;
	string s;
	cin>>sm>>s;
	j=0,out=0,m=0;
	while (j<=sm)
	{
	    v=(int)(s[j]-'0');
	    if (v==0 && m<=j)
	    {
		out++;
		m++;
		j++;
	    }
	    else
	    {
		m=m+v;
		j++;
	    }
	}
	cout<<"Case #"<<i+1<<": "<<out<<"\n";
    }
    return 0;
}
