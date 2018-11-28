#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

void rg(long long int &p, long long int &q) {
    long long int q1 = q, p1 = p;
    while (p1*q1 != 0) {
        if (p1 > q1) p1-=q1;
        else q1-=p1;
    }
    p = p/(p1+q1);
    q = q/(p1+q1);
}

int main() {
    freopen("A-small-attempt0.in.txt", "r", stdin);
    freopen("A-small-attempt0.out.txt", "w", stdout);
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T,pid=1;
	for (cin>>T;T--;) {
		printf("Case #%d: ",pid++);
        string str;
        cin >> str;
        int sid = str.find('/');
        string str1 = str.substr(0, sid+1);
        string str2 = str.substr(sid+1, str.length()-sid-1);
        long long int P = atoll(str1.c_str());
        long long int Q = atoll(str2.c_str());
        rg(P, Q);
        if (1 == P && 1 == Q) {printf("1\n");continue;}
        bool impossible = true;
        int tmp = 1;
        for (int i = 0; i <= 40;++i) {
            tmp = tmp<<1;
            if (Q == tmp) {impossible = false;break;}
        }
        if (impossible) {
            printf("impossible\n");
            continue;
        }
        
        int i = 1;
        for (; i <= 40; ++i) {
            P = P<<1;
            if (P >= Q) break;
        }
        printf("%d\n",i);
        
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}