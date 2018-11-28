#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <deque>

using namespace std;

#define MAX 1000

int main()
{
    int t,n;
    double v1[MAX], v2[MAX];
    scanf("%d", &t);
    for(int i=0; i<t; i++){
        printf("Case #%d: ", i+1);
        scanf("%d", &n);
        deque <double> d1,d2,p1, p2;
        for(int j=0; j<n; j++){
            scanf("%lf", &v1[j]);
        }
        for(int j=0; j<n; j++){
            scanf("%lf", &v2[j]);
        }
        sort(v1, v1+n);
        sort(v2, v2+n);
        for(int j=0; j<n; j++){
            d1.push_back(v1[j]);
            d2.push_back(v2[j]);
            p1.push_back(v1[j]);
            p2.push_back(v2[j]);
        }

        int dece=0, war=0;

        for(int j=0; j<n; j++){
            if(d1.front()>d2.front()){
                d1.pop_front();
                d2.pop_front();
                dece++;
            }
            else{
                d1.pop_front();
                d2.pop_back();
            }
        }

        for(int j=0; j<n; j++){
            if(p1.front()>p2.back()){
                p1.pop_front();
                p2.pop_front();
                war++;
            }
            else{
                int k=0;
                while(p2[k]<p1.front()){
                    k++;
                }
                p1.pop_front();
                p2.erase(p2.begin()+k);
            }
        }

        printf("%d %d\n", dece, war);

    }
}
