#include <sstream>
#include <string>
#include <math.h>
using namespace std;


bool isPalindrome(int x){
	ostringstream os;
	os<<x;
	string s=os.str();
	int i=0;
	int j=s.size()-1;
	while(i<j){
		if(s[i]!=s[j]){
			return false;
		}
		++i;
		--j;
	}
	return true;
}

int solve(int A, int B){
	bool isPal[1001];
	memset(isPal, 0, sizeof(isPal));
	for(int x=1;x<=B;++x){
		if(isPalindrome(x)){
			isPal[x]=true;
		}
	}
	int total=0;
	
	for(int x=1;x*x<=B;++x){
		if(x*x<A){
			continue;
		}
		if(isPal[x]&&isPal[x*x]){
			++total;
		}
	}
	return total;
}

int main(int argc, char *argv[]){
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;++c){
		int A, B;
		scanf("%d%d", &A, &B);
		int sol=solve(A, B);
		printf("Case #%d: %d\n", c, sol);
	}
	return 0;
}
