#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
	 int n,a1,a2,res1,res2;
	 cin>>n;
	 double naomi[n],ken[n],val;
	 
	 for(int k1=0;k1<n;k1++) {
	  cin>>naomi[k1];
	 }
	 for(int k1=0;k1<n;k1++) {
	  cin>>ken[k1];
	 }

	 res1=res2=a1=a2=0;
	 sort(naomi,naomi+n);
	 sort(ken,ken+n);

	 
	 while(a1<n && a2 < n) {
	  val = naomi[a1];
	  while(ken[a2] < val && a2 < n)
	   a2++;
	  if(a2 < n ) {
	   res2++;
	   a1++;
	   a2++;
	  } 
	 }
	 res2 = n - res2;
	 
	 a1=a2=res1=0;
	 while(a1<n && a2 < n) {
	  val = ken[a1];
	  while(naomi[a2] < val && a2 < n)
	   a2++;
	  if(a2 < n ) {
	   res1++;
	   a1++;
	   a2++;
	  } 
	 }

	 cout<<"Case #"<<i<<": "<<res1<<" "<<res2<<endl;
	}
	return 0;
}