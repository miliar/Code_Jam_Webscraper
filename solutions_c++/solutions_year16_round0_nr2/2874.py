#include <bits/stdc++.h>
using namespace std;

int main()
{
     freopen ("B-large.in","r",stdin); 
     freopen ("B-large.out","w",stdout);
     // freopen ("input.in","r",stdin); 
     int i,j,l,t,counter;
     string s;
     scanf("%d",&t);
     for(int casenum=1;casenum<=t;casenum++){
     	cin>>s;
     	l=s.size();
     	(s[l-1]=='+') ? counter=0 : counter=1;
     	for(i=l-2;i>=0;i--){
     		if(s[i]!=s[i+1])
     			counter++;
     	}
     	printf("Case #%d: %d\n",casenum,counter);
     }

	return 0;
}  