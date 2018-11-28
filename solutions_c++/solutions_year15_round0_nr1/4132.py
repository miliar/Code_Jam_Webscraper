/*
ID: k.kamal1
PROG: test
LANG: C++     
*/
#include <bits/stdc++.h>

using namespace std;

int main() {
    ofstream fout ("o.out");
    ifstream fin ("in.in");
    int tetC;
    fin >> tetC;
    for(int cnt = 0; cnt < tetC; cnt++)
    {
    	int num;
    	fin >> num;
    	long long ret = 0;
    	long long cur = 0;
    	for(int ct = 0; ct <= num; ct++)
    	{
    		char ch;
    		fin >> ch;
    		if(ch == '0')
    		continue;
    		
    		int curCh = ch - '0';
    		if(cur < ct)
    		{
    			ret += (ct - cur);
    			cur = ct;
    		}
    		
    		cur += curCh;
    		
    	}
    	fout << "Case #" << cnt+1 << ": " << ret << endl; 
     }
    return 0;
}
