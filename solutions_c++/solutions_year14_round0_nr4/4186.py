#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main(int argc, char * argv[])
{
    int t;
    scanf("%d", &t);
    while(t--) {
        int n;
        scanf("%d",&n);
        set<double> a, b;
        for(int i=0;i<n;++i) 
        {
            double ax;
            scanf("%lf",&ax);
            a.insert(ax);
        }
        for(int i=0;i<n;++i) 
        {
            double bx;
            scanf("%lf",&bx);
            b.insert(bx);
        }
        set<double>::iterator it;
/*
        printf("size of array = %d\n", n);
        printf("a array = ");
        for(it=a.begin();it!=a.end();++it) 
        {
            printf(" %lf", *it);
        }
        printf("\n");
        printf("b array = ");
        for(it=b.begin();it!=b.end();++it) 
        {
            printf(" %lf", *it);
        }
        printf("\n");
*/
        // a starts from small, tries to let b start from big
        // b starts from smallest bigger
        set<double> c(b);
        int y = 0, z = 0;
        set<double>::iterator ir, il;
        set<double>::reverse_iterator ira, irb;
        it = a.begin();
        ir = b.begin();
        ira = a.rbegin();
        irb = b.rbegin();
        if( *it > *irb )
        {
            y = z = n;
        } else if (*ira<*ir) {
            y = z = 0;
        } else {
            for(it=a.begin();it!=a.end();++it) 
            {
                // b find smallest item > *it if exist 
                // else smallest item , ++s
                ir = b.begin();
                while(*ir<*it && ir!=b.end()) {
                    ++ir;
                }
                if(ir == b.end()) {
                    ir = b.begin();
                    ++z;
                }
//                printf("a chu %lf, b chu %lf\n", *it, *ir);
                b.erase(ir);
            }
            int itn = n;
            while(itn>0) {
                il = a.begin();
//                il=il+(n-itn);
                it = c.begin();
                int idx = 0;
                bool allb = true;
                for(;idx < itn; ++idx)
                {
                    if(*il < *it) {
                        allb = false;
                        break;
                    }
                    ++il;
                    ++it;
                }
//                printf("itn = %d, idx = %d\n", itn, idx);
                if(allb) break;
                il = a.begin();
                a.erase(il);
                --itn;
            }
            y = itn;
/*
            set<double>::iterator ih;
            for(it=a.begin(), ih=c.begin()
                    ;it!=a.end() && ih!=c.end()
                    ;++it, ++ih) 
            {
                if(*it>*ih) ++y;
            }
            if(y==0) {
                set<double>::reverse_iterator ia;
                for(ia=a.rbegin(), ih=c.begin()
                    ;ia!=a.rend() && ih!=c.end()
                    ;++ia, ++ih) 
                {
                    if(*ia>*ih) ++y;
                }
            }
*/
        }
        static int id = 0;
        printf("Case #%d: %d %d \n", ++id, y, z);
    }
    return 0;
}
