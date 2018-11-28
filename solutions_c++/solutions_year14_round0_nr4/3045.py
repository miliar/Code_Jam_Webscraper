#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
#include<cmath>
#include<climits>
#include<queue>
#include<set>
#include<numeric>

#define VI vector<int>
#define PII pair<int,int>
#define mp make_pair
#define rep(i,a,b) for(i=(a); i<(b); i++)
#define repI(i,a,b) for(i=(a); i<=(b); i++)

using namespace std;
typedef unsigned long long int ulli;
typedef long long int lli;

int get_warCnt(vector<float>& naomi, vector<float>& ken)
{
    int beg1,beg2,end1,end2;
    beg1 = beg2 = 0;
    end1 = end2 = naomi.size()-1;
    int cnt = 0;
    while(end2>=beg2)
    {
        if (naomi[end1]-ken[end2] > 0.00000001) { cnt++; end1--; beg2++;}
        else { end1--; end2--; }
    }
    return cnt;
}

int get_dWarCnt(vector<float> naomi, vector<float> ken)
{
    int idx,cnt = 0; 
    int sz  = naomi.size();
    while (sz>0)
    {
        if (naomi[sz-1]- ken[sz-1] > 0.00000001)
        {
            cnt++;
            idx = upper_bound(naomi.begin(),naomi.end(),ken[0]) - naomi.begin();
            ken.erase(ken.begin());
            naomi.erase(naomi.begin()+idx);
        }
        else
        {
            ken.erase(ken.begin()+sz-1);
            naomi.erase(naomi.begin());
        }
        sz = naomi.size();
    }
    return cnt;
}

main()
{
    int T;
    cin >> T;
    int tot = T;
    int N;
    while(T--)
    {
        cin >> N;
        vector<float> naomi(N,0);
        vector<float> ken(N,0);
        for (int i=0; i<N; i++) cin >> naomi[i];
        for (int i=0; i<N; i++) cin >> ken[i];
        sort(naomi.begin(),naomi.end());
        sort(ken.begin(),ken.end());
        int warCnt  = get_warCnt(naomi,ken);
        int dWarCnt = get_dWarCnt(naomi,ken);
        cout << "Case #" << tot-T << ": " << dWarCnt << " " << warCnt << endl;
        /*
        for (int i=0; i<N; i++) cout << naomi[i] << " "; cout << endl;
        cout << accumulate(naomi.begin(),naomi.end(),0.0)/N << endl;
        for (int i=0; i<N; i++) cout << ken[i] << " "; cout << endl;
        cout << accumulate(ken.begin(),ken.end(),0.0)/N << endl;
        */
    }
}

