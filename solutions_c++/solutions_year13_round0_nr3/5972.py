#include<cstdio>
#include<cstring>
#include<iostream>
#include<conio.h>
#include<math.h>

using namespace std;
long long a,b;
long long arr[]={1,2,3,11,22};

int find(long sqrt)
{
	for(int i=0;i<4;i++)
	{
		if((arr[i]<=sqrt)&&(arr[i+1]>sqrt))
		{
			return i;
		}
		
	}
	return 4;
}

int main()
{
    
    int t,test;
    
    //long sqrt;

    
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d\n",&t);
    test=t;
    
    
    
    while(t--)
    {
              
            
            printf("Case #%d: ",test-t);
            
            scanf("%d %d",&a,&b);
            
            long long asqrt = sqrt(a);
            long long bsqrt = sqrt(b);
            
            int apos, bpos;
            apos = find(asqrt);
            bpos = find(bsqrt);
            int ans = bpos-apos;
            if((arr[apos]*arr[apos]-a)==0) ++ans;
            
            cout<<ans<<endl;
            
    }
            
            //getch();
}
                        
