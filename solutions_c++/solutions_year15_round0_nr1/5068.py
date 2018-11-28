#include<bits/stdc++.h>
using namespace std;

int readInt ()
{
	bool minus = false;
	int result = 0;
	char ch;
	ch = getchar();
	while (true)
	{
		if (ch == '-') break;
		if (ch >= '0' && ch <= '9') break;
		ch = getchar();
	}
	if (ch == '-') minus = true; else result = ch-'0';
	while (true) {
		ch = getchar();
		if (ch < '0' || ch > '9') break;
		result = result*10 + (ch - '0');
	}
	if (minus)
		return -result;
	else
		return result;
}


int main()
{
    int t,s,cnt=0,sofar,i,t1;
    char a[1001];

    t=readInt();
    t1=t;
    while(t--)
    {
        cnt=0;
        sofar=0;
        s=readInt();
        cin>>a;
        for(i=0;i<=s;i++)
        {
            if(sofar>=i)
            {sofar+=(a[i]-'0');}
            else
            {cnt+=(i-sofar);sofar+=((a[i]-'0')+i-sofar);}
        }
        cout<<"Case #"<<t1-t<<": "<<cnt<<endl;
    }
}
