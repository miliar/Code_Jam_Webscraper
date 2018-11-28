#include <bits/stdc++.h>
using namespace std;

int main()
{
     freopen ("C-small-attempt0.in","r",stdin); 
     freopen ("C-small-attempt0.out","w",stdout);
     // freopen ("input.in","r",stdin); 
     int i,j,n,t,k;
     string s;
     scanf("%d",&t);
     scanf("%d %d",&n,&j);

     int it=1;
     printf("Case #1:\n");
     for(i=1;i<n-1;i+=2)
     	for(j=2;j<n-1;j+=2){
			s.clear();	
     		for(k=0;k<=n-1;k++){
     			if(k==0 || k==n-1 || k==i || k==j)
     				s+='1';
     			else 
     				s+='0';
     		}
     		cout<<s<<" "<<3<<" "<<4<<" "<<5<<" "<<6<<" "<<7<<" "<<8<<" "<<9<<" "<<10<<" "<<11<<endl;
     	}
     printf("1000000000000001 3 4 5 6 7 8 9 10 11\n");

	return 0;
}  