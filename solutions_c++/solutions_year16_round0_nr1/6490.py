#include <bits/stdc++.h>
using namespace std;

int main() {
	 freopen("2016lar1.txt","r",stdin);
	    freopen("2016large1out.txt","w",stdout);
	int t,minimum;

	long int n,i,j,time,l;
	scanf("%d",&t);
for(int j=0;j<t;j++)
	{int A[10]={0};

	cin>>n;
	if(n==0)
        printf("Case #%d: INSOMNIA\n",j+1);
    else
    {long int k=1;
        minimum = *std::min_element(A,A+10);
        while(minimum==0)
        {
           l=k*n;
           while(l>0)
           {

               int d = l%10;

               A[d]++;
               l=l/10;
           }
k++;
           minimum = *std::min_element(A,A+10);
        }
      	printf("Case #%d: %d\n",j+1,(k-1)*n);
    }

	}

	// your code goes here
	return 0;
}
