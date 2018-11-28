#define _CRT_SECURE_NO_WARNINGS
//자료구조
#include <vector>
#include <list>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional> //greater, less

#include <tuple>
#include <utility>

#include <iostream>
#include <string>
#include <cstring>
#include <memory>
#include <cstdio>

using namespace std;

#define FOR (i,a,b) for (int i=(a);i<(b);++i)
#define FORD (i,a,b) for (int i=(a);i>(b);--i)
#define FORI (i,a,b) for (int i=(a);i<=(b);++i)
#define FORID (i,a,b) for (int i=(a);i>=(b);--i)
#define REP (i,a) for (int i=0;i<(a);++i)

int main() {
	freopen("C:\\Users\\seok\\Desktop\\A-small-attempt0.in", "r", stdin);
	freopen("C:\\Users\\seok\\Desktop\\out.txt", "w", stdout);
	int casenums = 0;
	scanf("%d", &casenums);
	for (int casenum = 1; casenum <= casenums; ++casenum) {
		vector<char> ret;
		int N = 0;
		scanf("%d", &N);
		multimap<int, int> P;
		int sum = 0;
		for (int i = 0; i < N; ++i) {
			int imsi = 0;
			scanf("%d", &imsi);
			P.insert(make_pair(imsi, i));
			sum += imsi;
		}
		N = sum;
		//cout << (P.begin()++)->first;		
		while (N > 0) {
			//multimap<int, int> backup=multimap<int,int>(P);//일단 백업
			//먼저 큰값 1개를 빼보자
			auto maxidx = P.end();
			maxidx--;			
			
			//char im = 'A' + maxidx->second;
			//char ims[10];
			//strcpy(ims, im);
			//string imsi(im);

			ret.push_back('A' + maxidx->second);
			/*for (int i = 0; i < ret.size(); ++i) {
				cout << ret[i] << " ";
			}*/

			if (maxidx->first - 1>0) P.insert(make_pair(maxidx->first-1, maxidx->second));
			P.erase(maxidx);
			N--;

			//cout << N << ">>"<< ceil(N / 2.0) << endl;
			if (P.lower_bound(floor(N / 2)+1) == P.end()) {//괜찮은경우
				ret.push_back(' ');
				continue;
			}
			else {//문제발생시 하나더 빼자 ㅋㅋ
				//cout << "double!";
				auto maxidx = P.end();
				maxidx--;
				ret.push_back('A' + maxidx->second);
				if (maxidx->first - 1>0) P.insert(make_pair(maxidx->first - 1, maxidx->second));
				P.erase(maxidx);
				N--;
				ret.push_back(' ');
			}
		}
		//입출력
		printf("Case #%d: ", casenum);
		for (int i = 0; i < ret.size(); ++i) {
			cout << ret[i];
		}
		cout << endl;
	}
}
