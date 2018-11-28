#include <iostream>
#include <string>
#include <cmath>
using namespace std;

long long int all_digits_not_seen(long long int arr[]){
    for(int i=0;i<10;i++)
        if(arr[i]!=1)
            return 1;
    return 0;
}

void mark_digits(long long int n, long long int arr[]){
    string s = to_string(n);
    for(int i=0;i<s.length();i++)
        arr[s[i]-'0'] = 1;
}

int main() {
    long long int test, n, i, j, arr[10], k;
	cin >> test;
	k = 1;
	while(test--){
	    cin >> n;
	    j = 1;
	    for(i=0;i<10;i++)   arr[i] = 0;
	    if(n==0)    cout << "Case #" << k << ": " << "INSOMNIA" << endl;
	    else{
	        while(all_digits_not_seen(arr)){
	            mark_digits(n*j, arr);
	            j++;
	        }
	        cout << "Case #" << k << ": " << n*(j-1) << endl;
	    }
	    k++;
	}
	return 0;
}
