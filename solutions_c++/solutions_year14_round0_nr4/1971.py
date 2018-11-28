#include "cstdio"
#include "cstring"
#include "vector"
#include "algorithm"
#include "utility"
#include "iostream"

using namespace std;

int main(void)
{
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        int n;
        vector<pair<double, char> > weights; 
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            double buff;
            cin >> buff;
            weights.push_back(make_pair(buff, 'x'));
        }
        for(int i=0;i<n;i++)
        {
            double buff;
            cin >> buff;
            weights.push_back(make_pair(buff, 'o'));
        }
        
        sort(weights.begin(), weights.end());
        
        printf("Case #%d:", test);
        int ansx = 0;
        int anso = 0;
        int bufo = 0;
        int bufx = 0;
        
        for(int i=0;i<2*n;i++)
        {
            if(weights[i].second == 'x')
            {
                bufx++;
                if(bufo > 0)
                {
                    bufo--;
                    ansx++;
                }
            }
            else
            {
                bufo++;
                if(bufx > 0)
                {
                    bufx--;
                    anso++;
                }
            }
        }
        
        printf(" %d %d\n",ansx,n-anso);
    }
    return 0;
}
