#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
    int tnum;
    scanf("%d",&tnum);
    for(int t = 1; t <= tnum; t++)
    {
        
        int la,lb,lk;
        scanf("%d%d%d",&la,&lb,&lk);
        //Less than Limit(a,b,c)
        
        const int n = 31;
        
        long long ans = 0;
        for(int sb = n-1; sb >= 0; sb--)
        if ((lb >> sb) & 1)
        {
            for(int sa = n-1; sa >= 0; sa--)
            if ((la >> sa) & 1)
            {
                int prea = (la >> (sa + 1)) << (sa + 1);
                int preb = (lb >> (sb + 1)) << (sb + 1);
                int ms = max(sa,sb);
                
                if ( ((prea & preb) >> ms) == (lk >> ms) )
                {
                    bool flag = true;
                    
                    long long p = 1;
                    for(int sk = ms - 1; sk >= min(sa,sb) && flag; sk--)
                    {
                        if ( (lk >> sk) & 1 )
                        {
                            if ( sk >= sa )
                            {
                                if ( ( (prea >> sk) & 1) == 0 )
                                {
                                    ans += p << (sa + sk + 1);
                                }
                                else
                                {
                                    ans += p << (sa + sk);
                                }
                            }
                            else
                            {
                                if ( ( (preb >> sk) & 1) == 0 )
                                {
                                    ans += p << (sb + sk + 1);
                                }
                                else
                                {
                                    ans += p << (sb + sk);
                                }
                            }
                        }
                        
                        if (sk >= sa)
                        {
                            if ( ( (prea >> sk) & 1) == 0) 
                            {
                                if ( (lk >> sk) & 1 )
                                    flag = false;
                                else
                                    p <<= 1;
                            }
                        }
                        else
                        {
                            if ( ( (preb >> sk) & 1) == 0)
                            {
                                if ( (lk >> sk) & 1 )
                                    flag = false;
                                else
                                    p <<= 1;
                            }
                        }
                    }
                    
                    for(int sk = min(sa,sb) - 1; sk >= 0 && flag; sk--)
                    {
                        if ( (lk >> sk) & 1 )
                        {
                            ans += (p * 3) << (sk * 2);
                        }
                        
                        if ( (lk >> sk) & 1 ) p *= 1;
                        else p *= 3;
                    }
                }
                else if ( ((prea & preb) >> ms) < (lk >> ms) )
                {
                    //All OK
                    ans += 1LL << (sb + sa);
                }
                
                //cout << sa << ' ' << sb << ' ' << ans << endl;
                //printf("Prea = %d Preb = %d\n",prea,preb);
            }
        }
 
        printf("Case #%d: ",t);       
        cout << ans << endl;
    }
    return 0;
}
