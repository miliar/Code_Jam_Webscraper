#include<iostream>
#include<queue>
using namespace std;
long long T, D, k, ret;

char c;
bool dbg = false;
int main(){
  cin >> T;
  for (long long t = 0;t < T;++t) {
    priority_queue<int> q, q2;
    cin >> D;
    for (long long  i=0; i<D; ++i) {
	    cin >> k;
	    q.push(k-1);q2.push(k);
    };
    ret = min(q.top()+1, q2.top());
    int time1 = 1, time2=0;
if (dbg)   cout << "\n\n\nbest ret = " << ret << "(time=" << time << ")" << endl;
    while (time2<ret) {
	    int x = q.top(); q.pop();
	    int s1 = x/2; int s2 = x-s1;
	    if (x==9) { s1=3; s2=6; }
	    q.push(s1); q.push(s2);
	    time1++;
	    if (q.top()+time1 < ret) {
		    ret = q.top()+time1;
	    };

	    //2
	    x = q2.top(); q2.pop();
	    s1 = x/2; s2 = x-s1;
	    if (x==9) { s1=3; s2=6; }
	    q2.push(s1); q2.push(s2);
	    time2++;
	    if (q2.top()+time2 < ret) {
		    ret = q2.top()+time2;
	    };

if (dbg)		    cout << "podzial: " << x << " na " << s1 << "," << s2 << endl;
if (dbg)		    cout << "best ret = " << ret << "(time=" << time << ")" << endl;

    };
if (dbg)    cout << "top=" << q.top() << endl;
    cout << "Case #" << t+1 << ": " << ret << endl;
  };

}
