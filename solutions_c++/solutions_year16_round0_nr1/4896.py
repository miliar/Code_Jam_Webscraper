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



long long solve(long long N) {
	int totalSeen = 0;
	int seen[10] = {0,0,0,0,0,0,0,0,0,0};
	bool seenAll = false;
	long long index = 1;
	if(N == 0) {
		return -1;
	} else {
		while(!seenAll) {
			long long currentN = N * index;

			long long tempN = currentN;
			while(tempN != 0) {
				int lastDigit = tempN % 10;
				if(seen[lastDigit] == 0) {
					seen[lastDigit] = 1;
					totalSeen++;

					if(totalSeen == 10) {
						return currentN;
					}
				}

				tempN /= 10;
			}

			index++;
		}
		return -1;
	}
}

int main(){
     long long T,N;
     cin>>T;
     for(int i = 1; i <= T; i++){
         cin>>N;

        long long ans = solve(N);
         
        if(ans == -1) {
        	cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        } else {
        	cout<<"Case #"<<i<<": "<<ans<<endl;
        }
     }
}