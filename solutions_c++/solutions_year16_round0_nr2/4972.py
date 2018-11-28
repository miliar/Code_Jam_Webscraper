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



int solve(string S) {
	bool fliped = false;
	int count = 0;
	for(int i = S.length() - 1; i >= 0 ; i--) {
		if(S[i] == '-' && fliped == false || S[i] == '+' && fliped == true) {
			count++;
			fliped = !fliped;
		}
	}
	return count;
}

int main(){
     int T;
     string S;
     cin>>T;
     for(int i = 1; i <= T; i++){
        cin>>S;
        int ans = solve(S);
         
        cout<<"Case #"<<i<<": "<<ans<<endl;
     }
}