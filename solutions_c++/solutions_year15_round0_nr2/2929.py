#include <iostream>
#include <queue>
#include <map>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <fstream>
#include <set>
using namespace std;
#define maxn 1005
int d[maxn];

int main(){
	ifstream fin("in.txt");
	ofstream fout("out.txt");
    int T,cas = 1,n;
    fin>>T;
    while(T--){
        fin>>n;
        int mx = 0;
		for(int i=0;i<n;++i)
			fin>>d[i],mx = max(mx,d[i]);
		int res = maxn;
		for(int up=mx;up>=1;--up)
		{
			int cur = 0;
			for(int i=0;i<n;++i)
			{
				if(d[i] > up)
				{
					cur += d[i]/up;
					if(d[i] % up == 0)
						cur -= 1;
				}
			}
			cur += up;
			res = min(res,cur);
		}
        fout<<"Case #"<<cas++<<": "<<res<<endl;
    }
	fout.close();
	fin.close();
    return 0;
}

