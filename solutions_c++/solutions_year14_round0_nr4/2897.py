#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<iostream>
#include<map>
#define REP(i,n) for(int i=0;i<n;i++)
#define IREP(i,n) for(int i=n-1;i>-1;i--)
typedef long long ll;

using namespace std;
double naomi[2111];
double naomi2[2111];
double ken[2111];
double ken2[2111];
int main()
{
#ifdef LOCALL
    freopen("D-large.in","r",stdin);
//    freopen("in","r",stdin);
    freopen("D-small-attempt1.out","w",stdout);
#endif
    int t;
    cin>>t;
    for(int kase = 1; kase <= t; kase ++)
    {
        int n;
        cin>>n;
        REP(i,n) {cin>>naomi[i];naomi2[i] = naomi[i];}
        REP(i,n) {cin>>ken[i];ken2[i] = ken[i];}

        int y,z;//y  Deceitful War,z  War. BOTH :Naomi will score
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        sort(naomi2,naomi2+n);
        sort(ken2,ken2+n);
        ken[n] = -1;
        y = z = 0;
        REP(i,n){//z
            int flag = 0;
            REP(j,n){
                if(ken[j]>naomi[i]){
                    ken[j]  = -1;
                    flag = 1;
                    break;
                }
            }
            naomi[i] = -1;
            if(!flag) {
                REP(j,n){
                    if(ken[j]!=-1){
                        ken[j] = -1;
                        break;
                    }
                }
                z++;
            }
        }

        IREP(j,n){//y
            int flag = 0;
            IREP(i,n){
                if(ken2[j]!=-1 && naomi2[i] != -1 && naomi2[i]>ken2[j]){
                    ken2[j] = -1;
                    naomi2[i] =-1;
                    flag = 1;
                    break;
                }
            }
            if(!flag){
                ken2[j] = -1;
                REP(i,n){
                    if(naomi2[i]!=-1){
                        naomi2[i] = -1;
                        break;
                    }
                }
            }
            else y++;
        }

        cout<<"Case #"<<kase<<": "<<y<<" "<<z<<endl;

    }
    return 0;
}

