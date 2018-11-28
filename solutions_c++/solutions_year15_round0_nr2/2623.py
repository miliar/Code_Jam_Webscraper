#include <iostream>
#include <vector>
#include <map>

using namespace std;
int t, d;
vector<int> p;


bool cmp(  int a, int b) {
    return a>b;
}

int mnt;

int rec(int t) {
    vector<int> tp;
    if (t >= mnt)
        return 12345;
    
    
    sort(p.begin(), p.end(), cmp);
    if (p[0] == 0) {
        //cout << "found"<<endl;
        return t;
    }
    
   /* for (int i = 0; i < p.size(); i++)
       cout << p[i]<<" ";
    cout << endl;
    */
    tp = p;
    for (int i = 0; i < p.size(); i++)
        p[i] = max(0, p[i]-1);
    //cout << "eat"<<endl;
    int t1 = rec(t+1);
    if (tp[0] == 1)
        return t1;
    int t2 = 100;
    
    p = tp;
    for (int i = 1; i < p[0]-1; i++) {
    p = tp;
    p.push_back(i);
        p[0] -= i;
        
//cout << "split"<<endl;
        t2 = min(rec(t+1), t2);
        
        p = tp;
    }
    
    p = tp;
    if (mnt > min(t1, t2))
        mnt = min(t1, t2);
    return min(t1, t2);
}

int main() {
	
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #"<<i <<": ";
		
        cin >> d;
        p.clear();
        p.assign(d, 0);
        for (int j = 0; j < d; j++)
            cin >> p[j];
        mnt = 12334;
        cout << rec(0)<<endl;
	}
	return 0;
}