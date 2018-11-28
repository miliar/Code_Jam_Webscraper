#include <bits/stdc++.h>
using namespace std;

int main() {
	 //freopen("2016BL.txt","r",stdin);
	    //freopen("2016Blarge.txt","w",stdout);
	int t;
string s;
int c;
	long int n,i,j;
	scanf("%d",&t);
for(int j=0;j<t;j++)
	{int k=0;
	cin>>s;

 for(int i =0;i<s.length();i++)
 {
     if(s[i]=='+')
     {
         c=1;
     }
     else
        c=0;
     while(s[i]==s[i+1] && i+1<s.length())
     {
         i++;

     }
     k++;
 }

if(c==1)
       k--;
      	printf("Case #%d: %d\n",j+1,k);

	}

	// your code goes here
	return 0;
}
