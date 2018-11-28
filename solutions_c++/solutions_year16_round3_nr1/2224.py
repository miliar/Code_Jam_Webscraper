#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

using namespace std;

#define s(n) scanf("%d",&n)
#define sl(n) scanf("%ld",&n)
#define sll(n) scanf("%lld",&n)
#define p(n) printf("%d ",n)
#define pl(n) printf("%ld ",n)
#define pll(n) printf("%lld\n",n)
#define fo(i,a,b) for(i=a;i<b;i++)
#define rf(i,a,b)	for(i=a;i>=b;i--)
# define toint(n)	(n-'0')
typedef long long ll;

int FindMin(int p[], int n) {
	int i, ind =0;
	fo(i,1,n) {
		if(p[i]<p[ind])
			ind  = i;
	}
	return ind;
}

int FindMax(int p[], int n) {
    int i, ind=0;
    fo(i,1,n) {
        if(p[i]>p[ind])
            ind = i;
    }
    return ind;
}

int FindSecondMax(int p[], int n, int person1) {
    int i, ind;
    if(person1==0) ind=1;
    else ind = 0;
    
    fo(i,1,n) {
        if((i!=person1)&&(p[i]>p[ind]))
            ind = i;
    }
    return ind;
}

int main(int argc, char const *argv[])
{
    //freopen("2016A-large.in","r",stdin);
    //freopen("2016A-large.out","w",stdout);
    int t,k,i,iniLog, n, p[30], person1, person2, x;
    ll ans,temp,tempAns,lim, totalpeople;
    int counter=0;
    
    s(t);
    fo(k,1,t+1)
    {
        totalpeople=0;
        s(n);
        fo(i,0,n) {
            s(p[i]);
            totalpeople += p[i];
        }
        
        printf("Case #%d: ",k);

        if(totalpeople%2==1) {
        	x = FindMin(p, n);
        	printf("%c ",(char)(65+x) );
        	p[x]--;
        	totalpeople--;
        }

        while(totalpeople>0) {
            person1 = FindMax(p, n);
            p[person1]--;
            totalpeople--;
            printf("%c", (char)(person1+65));
            
            if(totalpeople==0) break;
            
             person2 = FindSecondMax(p, n, person1);
             p[person2]--;
             totalpeople--;
             printf("%c ", (char)(person2+65));
            
            // cout<<"total = "<<totalpeople<<endl;
            // counter++;
            // if(counter>10) break;
        }
        
        printf("\n");
    }
    return 0;
}