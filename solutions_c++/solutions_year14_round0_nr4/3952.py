#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>

using namespace std;

int t, n, w1, w2;
double wood, hermax, hismax;
set<double> s1, s2, s3, s4;

int main() {
    int i, j;
    scanf("%d", &t);
    for (i=1; i<=t; ++i) {
        scanf("%d", &n);
        w1=0;
        hermax=0;
        hismax=0;
        for (j=0; j<n; ++j) {
            scanf("%lf", &wood);
            s1.insert(wood);
            if (hermax<wood) {
                hermax=wood;
            }
        }
        for (j=0; j<n; ++j) {
            scanf("%lf",&wood);
            s2.insert(wood);
            if (hismax<wood) {
                hismax=wood;
            }
        }
        s3=s1, s4=s2;
        while (w1<n && hermax>*(s2.begin())) {
                                //cout<<"cooo???   1"<<endl;
            w1++;
            if (*(s1.lower_bound(*(s2.begin())))==hermax) {
                break;
            }
            s1.erase(s1.lower_bound(*(s2.begin())));
            s2.erase(s2.begin());
        }
        s1.clear();
        s2.clear();
        w2=n;
        while (w2>0 && *(s3.begin())<hismax) {
                            //cout<<"cooo?  2"<<endl;
            w2--;
                            //cout<<"sprawdzam  "<<*(s4.lower_bound(*(s3.begin())))<<" "<<hismax<<endl;
            if (*(s4.lower_bound(*(s3.begin())))==hismax) {
                            //cout<<"dziala????"<<endl;
                break;
            }
                        //cout<<"tutaj?"<<endl;
            s4.erase(s4.lower_bound(*(s3.begin())));
                        //cout<<"a moze tutaj???"<<endl;
            s3.erase(s3.begin());
        }
        printf("Case #%d: %d %d\n", i, w1, w2);
    }
    return 0;
}
