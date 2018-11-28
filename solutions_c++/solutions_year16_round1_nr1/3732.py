    #include <bits/stdc++.h>
     
    using namespace std;
     
    string s;
    int n;
    deque<char> q;
     
    string calc() {
    	q.push_front(s[0]);
    	for(int i = 1; i < n; ++i) {
    		if(q[0] <= s[i]) {
    			q.push_front(s[i]);
    		}
    		else
    			q.push_back(s[i]);
    	}
    	string ans = s;
    	for(int i = 0; i < n; ++i) {
    		ans[i] = q[i];
    	}
    	q.clear();
    	return ans;
    }
     
     
    int main(void) {
    
    	ifstream fin;
    	fin.open("A-large(1).in");
     
    	ofstream fout;
    	fout.open("output.out");
    
     
    	int t;
    	fin>>t;
    	for(int tt = 1; tt <= t; ++tt) {
    		fin>>s;
    		n = s.size();
    		string ans = calc();
    		//printf("Case #%d: %d\n", tt, ans);
    		fout<<"Case #"<<tt<<": "<<ans<<"\n";
     
    	}
     
    	return 0;
     
    }