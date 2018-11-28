#include<bits/stdc++.h>
using namespace std;

struct star{
    int x,y;
    star(int x, int y): x(x), y(y){}
};

bool compareByX(const star &a, const star &b)
{
    return a.x < b.x;
}

double dist(star &a, star &b){
    return sqrt(((a.x-b.x)*(a.x-b.x)) + ((a.y-b.y)*(a.y-b.y)));
}



string solve(string S) {
	deque<char> ansQ;
	for(char c : S) {
		if(ansQ.size() > 0) {
			if(c < ansQ.front()) {
				ansQ.push_back(c);
			} else {
				ansQ.push_front(c);
			}
		} else {
			ansQ.push_back(c);
		}
	}

	string ans;
	for(char c : ansQ) {
		ans.push_back(c);
	}
	return ans;
}

int main(){
     long long T;
     cin>>T;
     string S;
     for(int i = 1; i <= T; i++){
         cin>>S;

        string ans = solve(S);
         
    	cout<<"Case #"<<i<<": "<<ans<<endl;

        
     }
}