// prob1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <queue>
#include <iostream>
#include <string>
using namespace std;

struct data
{
    string src, tgt;
}
temp;

string next_number(string s, string c)
{
    if(c == "") return c += s[0];
    
    string result = "";
    for(int i=c.length()-1; i>=0; i--) if(c[i] != s[s.length()-1])
    {
        for(int j=0; j<s.length()-1; j++) if(s[j] == c[i])
        {
            c[i] = s[j+1];
            for(int k=i+1; k<c.length(); k++) c[k] = s[0];
            return c;
        }
    }
    
    result += s[1];
    for(int i=0; i<c.length(); i++) result += s[0];
    return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
    freopen("input.txt","r",stdin); freopen("A-out.txt","w",stdout);
    char str[1000];
    int N;
	unsigned shy;
	unsigned int cnt, req;
	unsigned int temp;
    scanf("%d", &N);
    //cout << "Total = " << N << endl;
    for(int n=1; n<=N; n++)
    {
		cnt = req = 0;
        scanf("%d", &shy);
        scanf("%s", str);

		//cout << "shy = " << shy << " , str = " << str << endl;
		for(int i = 0; i <= shy; ++i)
		{
			temp = str[i] - '0';
			if(temp && (cnt < i))
			{
				req += (i - cnt);
				cnt += req;
			}
			cnt += temp;
		}
        printf("Case #%d: %d\n", n, req);
    }
	return 0;
}


