    //Other Includes
    #include<iostream>
    #include<algorithm>
    #include<cstring>
    #include<cassert>
    #include<cstdlib>
    #include<cstdio>
    #include<cmath>
    using namespace std;

    // Input macros
    #define s(n)                  scanf("%d",&n)
    #define sc(n)                 scanf("%c",&n)
    #define sl(n)                 scanf("%lld",&n)
    #define sf(n)                 scanf("%lf",&n)
    #define ss(n)                 scanf("%s",n)

    /*Main code begins now */

    void solve(int i){
        int r,t;
        scanf("%d%d",&r,&t);
        int result=0,diff = 1,a=0;
        while(t>0){
            a= ((r+diff)*(r+diff) - (r+diff-1)*(r+diff-1));
            if(t >= a){
                t -= a;
                result++;
                diff+=2;
            }
            else
                break;
        }
        printf("Case #%d: %d\n",i,result);
	}
    int main()
    {
    	int tcase,i=1;
		scanf("%d",&tcase);
		while(i <= tcase){
            solve(i);
            i++;
        }
    return 0;
    }
