#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	int t,n,i,score,np,T,k;
	float bn[1050],bk[1050];
	cin >> T;
	for(k=1;k<=T;k++){
	cout << "Case #" << k << ": ";
	cin >> n;
	score = 0;
	np = 0;
	for(i=0;i<n;i++)
	{
		cin >> bn[i];
	}
	for(i=0;i<n;i++)
	{
		cin >> bk[i];
	}
	sort(bn,bn+n);
	sort(bk,bk+n);
	for(i=0;i<n;i++)
	{
		if (bn[n-np-1]>bk[n-i-1]){
			score++;
	    	np++;
	    }
	}
	cout << score << " ";
	score = 0;
   	np = 0;
	for(i=0;i<n;i++)
	{
		if (bk[n-np-1]<bn[n-i-1]){
			score++;
	    }
	    else
        	np++;
	}
	cout << score << "\n";
	}
}
