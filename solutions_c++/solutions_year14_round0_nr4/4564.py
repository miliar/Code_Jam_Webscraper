#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
 
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("D.out", "w", stdout);
	int test;
	double k[1010],na[1010];
	scanf("%d",&test);
	int it=1;
	while(test--)
    {
    	int n;
        cin>>n;
        
        for(int i=0;i<n;i++)
            cin>>na[i];
            
        for(int i=0;i<n;i++)
            cin>>k[i];
            
        sort(na,na+n);
        sort(k,k+n);
        
        int decitwar=0,actualwar=0;
        int left=0,right=0;
        
        while(left<n && right<n)
        {
            if(na[left]>k[right])
            {
                decitwar++;
                left++;
                right++;
            }
            else
                left++;
        }
        left=0,right=0;
        while(left<n && right<n)
        {
            if(na[left]<k[right])
            {
                actualwar++;
                left++;
                right++;
            }
            else
                right++;
        }
        printf("Case #%d: %d %d\n",(it++),decitwar,n-actualwar);
    }
 
	return 0;
}
 
