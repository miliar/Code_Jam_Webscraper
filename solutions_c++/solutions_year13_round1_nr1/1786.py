#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<iterator>
using namespace std;

inline int scan()
{
    int po=0;
    char ch;
    ch=getchar_unlocked();
    while(ch<'0' || ch>'9')
        ch=getchar_unlocked();
    while(ch>='0' && ch<='9')
    {
        po=(po<<3)+(po<<1)+ch-'0';
        ch=getchar_unlocked();
    }
    return po;
}

int main()
{
	int test;
	test = scan();
	for(int k = 0; k<test; k++)
	{
		int paint = 0, count = 0;
		int r, t;
		r = scan(); 
		t = scan();
		do
		{
			count++;
			paint+=((r+1)*(r+1)-r*r);
			r+=2;
		}while(paint<t);
		if(paint>t)
			count--;
		cout<<"Case #"<<k+1<<": "<<count<<endl;
	}
	return 0;
}
