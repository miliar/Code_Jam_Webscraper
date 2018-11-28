#include <iostream>
#include <cstdio>
#include <cmath>
#include <fstream>
using namespace std;

bool judge(int originalNumber) {  
    int palindrome = 0;  
    int origin = originalNumber;  
   
    while(originalNumber != 0) {  
        palindrome = palindrome * 10 + originalNumber % 10;  
        originalNumber /= 10;  
    }  
  
    return palindrome == origin ;  
}  

int main()
{
	ifstream infile("C-small-attempt0.in");
	ofstream outfile("ans.out");
	int n, head, tail, ans;
	double h, t;
	infile >> n;
	for(int cnt=1; cnt<=n; cnt++){
		ans=0;
		infile >> head >> tail;
		h = sqrt(head)-1e-6;
		t = sqrt(tail)-1e-6;
		for(int i=int(h); i<=int(t)+1; i++)
			if(i*i>=head && i*i<=tail)
				if(judge(i*i) && judge(i))
					ans++;
		outfile << "Case #" << cnt << ": " << ans << endl;
	}
	return 0;
}
