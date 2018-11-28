#include <cstdio>
#include <vector>
using namespace std;

#define Long long long
vector < Long > fair;
int T;
FILE *fin = fopen("C-small.in" , "r");
FILE *fout= fopen("C-small.out", "w");

inline bool palindrome(Long n){
	vector < int > v1;
	vector < int > v2;
	while(n){
		v1.push_back(n % 10);
		n /= 10;
	}
	v2 = v1;
	reverse(v2.begin() , v2.end());
	return v1 == v2;
}
int b_search(Long n){
	int low = 0 , high = (int)(fair.size()) - 1;
	int ans;
	while(low <= high){
		int mid = (low + high) / 2;
		if(fair[mid] > n)
			high = mid - 1;
		else if(fair[mid] < n){
			ans = mid;
			low = mid + 1;
		}
		else if(fair[mid] == n)
			return mid;
	}
	return ans;
}
int main(){
	for(Long n = 1 ; n * n <= 1000 ; n++)
		if(palindrome(n) && palindrome(n * n))
			fair.push_back(n * n);
	
	fscanf(fin , "%d" , &T);
	for(int t = 1 ; t <= T ; t++){
		Long A , B;
		fscanf(fin , "%lld %lld" , &A , &B);
		int low = b_search(A);
		int high= b_search(B);
		if(fair[low] != A)
			fprintf(fout , "Case #%d: %d\n" , t , high - low);
		else
			fprintf(fout , "Case #%d: %d\n" , t , high - low + 1);
	}
	return 0;
}