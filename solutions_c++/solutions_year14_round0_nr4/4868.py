#include<iostream>
#include<cstdio>
#include<cmath>
#include<sstream>
#include<ctime>
#include<cstring>
#include<cstdlib>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<map>
#include<set>
#define mp make_pair
#define pb push_back
#define max(a,b)a>b?a:b
#define min(a,b)a<b?a:b
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

int main ()
{
    freopen("out.txt","w",stdout);
    //freopen("in.txt","r",stdin);
    int testCase,y,bricks;
    cin>>testCase;
    for(int qq=1;qq<=testCase;qq++)
    {
        cin>>bricks;
        vector<double> naomi,ken;
        double x;
        int counter,n_big,n_small,k_big,k_small;
        counter=bricks;
        n_big=k_big=counter-1;
        n_small=k_small=0;
        
        for(int i=1;i<=bricks;i++)
        {
            cin>>x;
            naomi.pb(x);
        }

        for(int i=1;i<=bricks;i++)
        {
            cin>>x;
            ken.pb(x);
        }
        
        sort(naomi.begin(),naomi.end());
        sort(ken.begin(),ken.end());
        
        
        counter=bricks;
        n_big=k_big=counter-1;
        n_small=k_small=0;
        int points=0;
        while(counter--)
        {
            if(naomi[n_big]>ken[k_big])
            {
                n_big--;
                k_big--;
                points++;
                
            }
            else
            {
                n_small++;
                k_big--;
            }
        }
        printf("Case #%d: %d ", qq,points);
        
        counter=bricks;
        n_big=k_big=counter-1;
        n_small=k_small=0;
        points=0;
        
        while(bricks--)
        {
            if(naomi[n_big]>ken[k_big])
            {
                n_big--;
                k_small++;
                points++;
            }
            
            else
            {
                n_big--;
                k_big--;
                
            }
        }
        cout<<points<<endl;
    }
    return 0;
}




